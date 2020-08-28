from kivy.app import App
from kivymd.theming import ThemeManager
from datetime import datetime
from kivymd.toast import toast
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
import requests
import json


class Y(FloatLayout):
    pass


class N(FloatLayout):
    pass


class MainApp(App):

    def patch_team(self):

        if self.root.ids.devtext.text != "":
            name = ('{"' + self.root.ids.devtext.text + '": {"Checkpoint1": {"Zeit": "0"}, "Checkpoint2": {"Zeit": "0"}, "Checkpoint3": {"Zeit": "0"}, "Checkpoint4": {"Zeit": "0"}, "Checkpoint5": {"Zeit": "0"}, "Start": {"Zeit": "0"}, "Ziel": {"Zeit": "0"}}}')
            to_database = json.loads(name)
            requests.patch(url="https://testapp-4a3b0.firebaseio.com/.json", json=to_database)
        else:
            toast("insufficient name")

    def check_reset(self):

        if self.root.ids.devtext.text != "":
            f = open("Stats.txt", "w+")
            f.write(self.root.ids.devtext.text)
            f.close()
            toast("Checkpoint changed")
        else:
            toast("not a valid checkpoint")


    def show_popup_n(self):
        show = N()
        popup_window = Popup(title="", content=show, size_hint=(None, None), size=(220, 100))
        popup_window.open()

    def weiter_btn(self):

        result = requests.get("https://testapp-4a3b0.firebaseio.com/.json")
        data = json.loads(result.content.decode())
        key = data.keys()
        if self.root.ids.team_name.text == "admin":
            self.root.ids.screen_manager.current = 'dev'

        elif self.root.ids.team_name.text in key and self.root.ids.team_name.text != "admin":
            f = open("Stats.txt", "a+")
            f.close()

            self.root.ids.start.text = "Startzeit: "
            self.root.ids.check1.text = "Zwischenzeit 1: "
            self.root.ids.check2.text = "Zwischenzeit 2: "
            self.root.ids.check3.text = "Zwischenzeit 3: "
            self.root.ids.check4.text = "Zwischenzeit 4: "
            self.root.ids.check5.text = "Zwischenzeit 5: "
            self.root.ids.ziel.text = "Final-Zeit: "

            self.root.ids.screen_manager.current = 'time'

        else:
            self.show_popup_n()

    def starttime(self):

        wert = self.root.ids.input.text

        result = requests.get("https://testapp-4a3b0.firebaseio.com/.json")
        data = json.loads(result.content.decode())
        key = data.keys()
        if self.root.ids.team_name.text in key:

            if wert == "56547234":  # Start
                f = open("Stats.txt", "w+")
                f.write("S")
                f.close()
                now = datetime.now()
                print("Startzeit: ", now.strftime("%H:%M:%S"))

                z = now.strftime("%H:%M:%S")
                b = '"}'
                x = '{"Zeit": "'

                name = (x + z + b)

                to_database = json.loads(name)
                requests.patch(
                    url="https://testapp-4a3b0.firebaseio.com/" + self.root.ids.team_name.text + "/Start.json",
                    json=to_database)

                self.root.ids.Start.text = z

                toast("Startzeit: " + now.strftime("%H:%M:%S"))

            elif wert == "95761243":  # Checkpoint1

                f = open("Stats.txt", "r")
                content = f.read()

                if content == "S":

                    f = open("Stats.txt", "a+")
                    f.write("1")
                    f.close()

                    result = requests.get(
                        "https://testapp-4a3b0.firebaseio.com/" + self.root.ids.team_name.text + "/Start/Zeit.json")
                    data_start = json.loads(result.content.decode())

                    then1 = datetime.now()
                    print("1. Checkpoint-Zeit: ", then1.strftime("%H:%M:%S"))
                    s11 = data_start
                    s21 = then1.strftime("%H:%M:%S")
                    fmt = '%H:%M:%S'
                    tdelta1 = datetime.strptime(s21, fmt) - datetime.strptime(s11, fmt)
                    print("1. Zeitabschnitt: ", tdelta1)

                    d = str(tdelta1)
                    b = '"}'
                    x = '{"Zeit": "'

                    name = (x + d + b)

                    to_database = json.loads(name)
                    requests.patch(
                        url="https://testapp-4a3b0.firebaseio.com/" + self.root.ids.team_name.text +
                            "/Checkpoint1.json",
                        json=to_database)

                    self.root.ids.Start.text = data_start
                    self.root.ids.Check1.text = d

                    toast("Zeit: " + d)

                else:
                    toast("Ungültiger Checkpoint")
                    print("Fehler")

            elif wert == "59129853":  # Checkpoint2

                f = open("Stats.txt", "r")
                content = f.read()

                if content == "S1":

                    f = open("Stats.txt", "a+")
                    f.write("2")
                    f.close()

                    result = requests.get(
                        "https://testapp-4a3b0.firebaseio.com/" + self.root.ids.team_name.text +
                        "/Start/Zeit.json")
                    data_start = json.loads(result.content.decode())

                    result2 = requests.get(
                        "https://testapp-4a3b0.firebaseio.com/" + self.root.ids.team_name.text +
                        "/Checkpoint1/Zeit.json")
                    data_check1 = json.loads(result2.content.decode())

                    then2 = datetime.now()
                    print("2. Checkpoint-Zeit: ", then2.strftime("%H:%M:%S"))
                    s12 = data_start
                    s22 = then2.strftime("%H:%M:%S")
                    fmt = '%H:%M:%S'
                    tdelta2 = datetime.strptime(s22, fmt) - datetime.strptime(s12, fmt)
                    print("2. Zeitabschnitt: ", tdelta2)

                    e = str(tdelta2)
                    b = '"}'
                    x = '{"Zeit": "'

                    name = (x + e + b)

                    to_database = json.loads(name)
                    requests.patch(
                        url="https://testapp-4a3b0.firebaseio.com/" + self.root.ids.team_name.text +
                            "/Checkpoint2.json",
                        json=to_database)

                    self.root.ids.Start.text = data_start
                    self.root.ids.Check1.text = data_check1
                    self.root.ids.Check2.text = e

                    toast("Zeit: " + e)

                else:
                    toast("Ungültiger Checkpoint")
                    print("Fehler")

            elif wert == "98716322":  # Checkpoint3

                f = open("Stats.txt", "r")
                content = f.read()

                if content == "S12":

                    f = open("Stats.txt", "a+")
                    f.write("3")
                    f.close()

                    result = requests.get(
                        "https://testapp-4a3b0.firebaseio.com/" + self.root.ids.team_name.text +
                        "/Start/Zeit.json")
                    data_start = json.loads(result.content.decode())

                    result2 = requests.get(
                        "https://testapp-4a3b0.firebaseio.com/" + self.root.ids.team_name.text +
                        "/Checkpoint1/Zeit.json")
                    data_check1 = json.loads(result2.content.decode())

                    result3 = requests.get(
                        "https://testapp-4a3b0.firebaseio.com/" + self.root.ids.team_name.text +
                        "/Checkpoint2/Zeit.json")
                    data_check2 = json.loads(result3.content.decode())

                    then3 = datetime.now()
                    print("3. Checkpoint-Zeit: ", then3.strftime("%H:%M:%S"))
                    s13 = data_start
                    s23 = then3.strftime("%H:%M:%S")
                    fmt = '%H:%M:%S'
                    tdelta3 = datetime.strptime(s23, fmt) - datetime.strptime(s13, fmt)
                    print("3. Zeitabschnitt: ", tdelta3)

                    g = str(tdelta3)
                    b = '"}'
                    x = '{"Zeit": "'

                    name = (x + g + b)

                    to_database = json.loads(name)
                    requests.patch(
                        url="https://testapp-4a3b0.firebaseio.com/" + self.root.ids.team_name.text +
                            "/Checkpoint3.json",
                        json=to_database)

                    self.root.ids.Start.text = data_start
                    self.root.ids.Check1.text = data_check1
                    self.root.ids.Check2.text = data_check2
                    self.root.ids.Check3.text = g

                    toast("Zeit: " + g)

                else:
                    toast("Ungültiger Checkpoint")
                    print("Fehler")

            elif wert == "23475641":  # Checkpoint4

                f = open("Stats.txt", "r")
                content = f.read()

                if content == "S123":

                    f = open("Stats.txt", "a+")
                    f.write("4")
                    f.close()

                    result = requests.get(
                        "https://testapp-4a3b0.firebaseio.com/" + self.root.ids.team_name.text +
                        "/Start/Zeit.json")
                    data_start = json.loads(result.content.decode())

                    result2 = requests.get(
                        "https://testapp-4a3b0.firebaseio.com/" + self.root.ids.team_name.text +
                        "/Checkpoint1/Zeit.json")
                    data_check1 = json.loads(result2.content.decode())

                    result3 = requests.get(
                        "https://testapp-4a3b0.firebaseio.com/" + self.root.ids.team_name.text +
                        "/Checkpoint2/Zeit.json")
                    data_check2 = json.loads(result3.content.decode())

                    result4 = requests.get(
                        "https://testapp-4a3b0.firebaseio.com/" + self.root.ids.team_name.text +
                        "/Checkpoint3/Zeit.json")
                    data_check3 = json.loads(result4.content.decode())

                    then4 = datetime.now()
                    print("4. Checkpoint-Zeit: ", then4.strftime("%H:%M:%S"))
                    s14 = data_start
                    s24 = then4.strftime("%H:%M:%S")
                    fmt = '%H:%M:%S'
                    tdelta4 = datetime.strptime(s24, fmt) - datetime.strptime(s14, fmt)
                    print("4. Zeitabschnitt: ", tdelta4)

                    i = str(tdelta4)
                    b = '"}'
                    x = '{"Zeit": "'

                    name = (x + i + b)

                    to_database = json.loads(name)
                    requests.patch(
                        url="https://testapp-4a3b0.firebaseio.com/" + self.root.ids.team_name.text +
                            "/Checkpoint4.json",
                        json=to_database)

                    self.root.ids.Start.text = data_start
                    self.root.ids.Check1.text = data_check1
                    self.root.ids.Check2.text = data_check2
                    self.root.ids.Check3.text = data_check3
                    self.root.ids.Check4.text = i

                    toast("Zeit: " + i)

                else:
                    toast("Ungültiger Checkpoint")
                    print("Fehler")

            elif wert == "91175234":  # Checkpoint5

                f = open("Stats.txt", "r")
                content = f.read()

                if content == "S1234":

                    f = open("Stats.txt", "a+")
                    f.write("5")
                    f.close()

                    result = requests.get(
                        "https://testapp-4a3b0.firebaseio.com/" + self.root.ids.team_name.text +
                        "/Start/Zeit.json")
                    data_start = json.loads(result.content.decode())

                    result2 = requests.get(
                        "https://testapp-4a3b0.firebaseio.com/" + self.root.ids.team_name.text +
                        "/Checkpoint1/Zeit.json")
                    data_check1 = json.loads(result2.content.decode())

                    result3 = requests.get(
                        "https://testapp-4a3b0.firebaseio.com/" + self.root.ids.team_name.text +
                        "/Checkpoint2/Zeit.json")
                    data_check2 = json.loads(result3.content.decode())

                    result4 = requests.get(
                        "https://testapp-4a3b0.firebaseio.com/" + self.root.ids.team_name.text +
                        "/Checkpoint3/Zeit.json")
                    data_check3 = json.loads(result4.content.decode())

                    result5 = requests.get(
                        "https://testapp-4a3b0.firebaseio.com/" + self.root.ids.team_name.text +
                        "/Checkpoint4/Zeit.json")
                    data_check4 = json.loads(result5.content.decode())

                    then5 = datetime.now()
                    print("5. Checkpoint-Zeit: ", then5.strftime("%H:%M:%S"))
                    s15 = data_start
                    s25 = then5.strftime("%H:%M:%S")
                    fmt = '%H:%M:%S'
                    tdelta5 = datetime.strptime(s25, fmt) - datetime.strptime(s15, fmt)
                    print("5. Zeitabschnitt: ", tdelta5)

                    k = str(tdelta5)
                    b = '"}'
                    x = '{"Zeit": "'

                    name = (x + k + b)

                    to_database = json.loads(name)
                    requests.patch(
                        url="https://testapp-4a3b0.firebaseio.com/" + self.root.ids.team_name.text +
                            "/Checkpoint5.json",
                        json=to_database)
                    self.root.ids.Start.text = data_start
                    self.root.ids.Check1.text = data_check1
                    self.root.ids.Check2.text = data_check2
                    self.root.ids.Check3.text = data_check3
                    self.root.ids.Check4.text = data_check4
                    self.root.ids.Check5.text = k

                    toast("Zeit: " + k)

                else:
                    toast("Ungültiger Checkpoint")
                    print("Fehler")

            elif wert == "99993451":  # Ziel

                f = open("Stats.txt", "r")
                content = f.read()

                if content == "S12345":

                    result = requests.get(
                        "https://testapp-4a3b0.firebaseio.com/" + self.root.ids.team_name.text + "/Start/Zeit.json")
                    data_start = json.loads(result.content.decode())

                    result2 = requests.get(
                        "https://testapp-4a3b0.firebaseio.com/" + self.root.ids.team_name.text +
                        "/Checkpoint1/Zeit.json")
                    data_check1 = json.loads(result2.content.decode())

                    result3 = requests.get(
                        "https://testapp-4a3b0.firebaseio.com/" + self.root.ids.team_name.text +
                        "/Checkpoint2/Zeit.json")
                    data_check2 = json.loads(result3.content.decode())

                    result4 = requests.get(
                        "https://testapp-4a3b0.firebaseio.com/" + self.root.ids.team_name.text +
                        "/Checkpoint3/Zeit.json")
                    data_check3 = json.loads(result4.content.decode())

                    result5 = requests.get(
                        "https://testapp-4a3b0.firebaseio.com/" + self.root.ids.team_name.text +
                        "/Checkpoint4/Zeit.json")
                    data_check4 = json.loads(result5.content.decode())

                    result6 = requests.get(
                        "https://testapp-4a3b0.firebaseio.com/" + self.root.ids.team_name.text +
                        "/Checkpoint5/Zeit.json")
                    data_check5 = json.loads(result6.content.decode())

                    then6 = datetime.now()
                    print("6. Checkpoint-Zeit: ", then6.strftime("%H:%M:%S"))
                    s16 = data_start
                    s26 = then6.strftime("%H:%M:%S")
                    fmt = '%H:%M:%S'
                    tdelta6 = datetime.strptime(s26, fmt) - datetime.strptime(s16, fmt)
                    print("6. Zeitabschnitt: ", tdelta6)

                    m = str(tdelta6)
                    b = '"}'
                    x = '{"Zeit": "'

                    name = (x + m + b)

                    to_database = json.loads(name)
                    requests.patch(
                        url="https://testapp-4a3b0.firebaseio.com/" + self.root.ids.team_name.text + "/Ziel.json",
                        json=to_database)
                    self.root.ids.Start.text = data_start
                    self.root.ids.Check1.text = data_check1
                    self.root.ids.Check2.text = data_check2
                    self.root.ids.Check3.text = data_check3
                    self.root.ids.Check4.text = data_check4
                    self.root.ids.Check5.text = data_check5
                    self.root.ids.Ziel.text = m

                    a = '{"'
                    c = self.root.ids.team_name.text
                    n = '": "'

                    name2 = (a + c + n + m + b)

                    to2_database = json.loads(name2)
                    requests.patch(
                        url="https://testapp-4a3b0.firebaseio.com/Zieleinlauf.json",
                        json=to2_database)

                    toast("Zeit: " + m)

                else:
                    toast("Ungültiger Checkpoint")
                    print("Fehler")

            else:
                toast("Ungültiger Checkpoint")
                print("Fehler")
        else:
            toast("Teamname eingeben!")

    theme_cls = ThemeManager()
    theme_cls.primary_palette = 'Blue'
    theme_cls.accent_palette = 'Red'
    theme_cls.theme_style = 'Light'


if __name__ == '__main__':
    MainApp().run()
