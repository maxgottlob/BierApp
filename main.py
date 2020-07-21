from kivy.app import App
from kivymd.theming import ThemeManager
from kivy.core.window import Window
from datetime import datetime
from kivymd.toast import toast
import requests
import json

Window.size = (300, 500)


class MainApp(App):
    url = 'https://testapp-4a3b0.firebaseio.com/.json'

    def get_teams(self):

        result = requests.get("https://testapp-4a3b0.firebaseio.com/.json")
        data = json.loads(result.content.decode())
        Namen = list(data.keys())
        global name1
        name1 = (Namen[0])
        global name2
        name2 = (Namen[1])
        global name3
        name3 = (Namen[2])
        global name4
        name4 = (Namen[3])
        global name5
        name5 = (Namen[4])



    def weiter_btn(self):

        b = '":{"Start": "0", "Checkpoint 1": "0", "Checkpoint 2": "0", "Checkpoint 3": "0", "Checkpoint 4": "0", "Checkpoint 5": "0", "Ziel": "0"}}'
        y = self.root.ids.team_name.text
        x = '{"'
        name = (x + y + b)

        to_database = json.loads(name)
        requests.patch(url=self.url, json=to_database)

    def starttime(self, _keys=[]):

        input = self.root.ids.input.text

        if input == "56547234" and 0 not in _keys:
            _keys.append(0)
            global now
            now = datetime.now()
            print("Startzeit: ", now.strftime("%H:%M:%S"))

            global z
            z = now.strftime("%H:%M:%S")
            b = '", "Checkpoint 1": "0", "Checkpoint 2": "0", "Checkpoint 3": "0", "Checkpoint 4": "0", "Checkpoint 5": "0", "Ziel": "0"}}'
            a = '":{"Start": "'
            y = self.root.ids.team_name.text
            x = '{"'

            name = (x + y + a + z + b)

            to_database = json.loads(name)
            requests.patch(url=self.url, json=to_database)

            result = requests.get("https://testapp-4a3b0.firebaseio.com/" + self.root.ids.team_name.text + ".json")
            data = json.loads(result.content.decode())
            self.root.ids.Start.text = "Startzeit: " + data.get("Start")
            self.root.ids.Check1.text = "Delta Checkpoint 1: "
            self.root.ids.Check2.text = "Delta Checkpoint 2: "
            self.root.ids.Check3.text = "Delta Checkpoint 3: "
            self.root.ids.Check4.text = "Delta Checkpoint 4: "
            self.root.ids.Check5.text = "Delta Checkpoint 5: "
            self.root.ids.Ziel.text = "Delta Ziel: "

            toast("Startzeit: " + data.get("Start"))






        elif input == "95761243" and 1 not in _keys and 0 in _keys:
            _keys.append(1)
            then1 = datetime.now()
            print("1. Checkpoint-Zeit: ", then1.strftime("%H:%M:%S"))
            s11 = now.strftime("%H:%M:%S")
            s21 = then1.strftime("%H:%M:%S")
            FMT = '%H:%M:%S'
            tdelta1 = datetime.strptime(s21, FMT) - datetime.strptime(s11, FMT)
            print("1. Zeitabschnitt: ", tdelta1)

            global d
            d = str(tdelta1)
            b = '", "Checkpoint 1": " '
            c = '", "Checkpoint 2": "0", "Checkpoint 3": "0", "Checkpoint 4": "0", "Checkpoint 5": "0", "Ziel": "0"}}'
            a = '":{"Start": "'
            y = self.root.ids.team_name.text
            x = '{"'

            name = (x + y + a + z + b + d + c)

            to_database = json.loads(name)
            requests.patch(url=self.url, json=to_database)

            result = requests.get("https://testapp-4a3b0.firebaseio.com/" + self.root.ids.team_name.text + ".json")
            data = json.loads(result.content.decode())
            self.root.ids.Check1.text = "Delta Checkpoint 1: " + data.get("Checkpoint 1")
            self.root.ids.Check2.text = "Delta Checkpoint 2: "
            self.root.ids.Check3.text = "Delta Checkpoint 3: "
            self.root.ids.Check4.text = "Delta Checkpoint 4: "
            self.root.ids.Check5.text = "Delta Checkpoint 5: "
            self.root.ids.Ziel.text = "Delta Ziel: "

            toast("Zeit: " + data.get("Checkpoint 1"))

        elif input == "59129853" and 2 not in _keys and 1 in _keys:
            _keys.append(2)
            then2 = datetime.now()
            print("2. Checkpoint-Zeit: ", then2.strftime("%H:%M:%S"))
            s12 = now.strftime("%H:%M:%S")
            s22 = then2.strftime("%H:%M:%S")
            FMT = '%H:%M:%S'
            tdelta2 = datetime.strptime(s22, FMT) - datetime.strptime(s12, FMT)
            print("2. Zeitabschnitt: ", tdelta2)

            global e
            e = str(tdelta2)
            b = '", "Checkpoint 1": "'
            c = '", "Checkpoint 2": "'
            f = '", "Checkpoint 3": "0", "Checkpoint 4": "0", "Checkpoint 5": "0", "Ziel": "0"}}'
            a = '":{"Start": "'
            y = self.root.ids.team_name.text
            x = '{"'

            name = (x + y + a + z + b + d + c + e + f)

            to_database = json.loads(name)
            requests.patch(url=self.url, json=to_database)  # z = Startzeit // d = Check1 // e = Check2

            to_database = json.loads(name)
            requests.patch(url=self.url, json=to_database)

            result = requests.get("https://testapp-4a3b0.firebaseio.com/" + self.root.ids.team_name.text + ".json")
            data = json.loads(result.content.decode())
            self.root.ids.Check2.text = "Delta Checkpoint 2: " + data.get("Checkpoint 2")
            self.root.ids.Check3.text = "Delta Checkpoint 3: "
            self.root.ids.Check4.text = "Delta Checkpoint 4: "
            self.root.ids.Check5.text = "Delta Checkpoint 5: "
            self.root.ids.Ziel.text = "Delta Ziel: "

            toast("Zeit: " + data.get("Checkpoint 2"))

        elif input == "98716322" and 3 not in _keys and 2 in _keys:
            _keys.append(3)
            then3 = datetime.now()
            print("3. Checkpoint-Zeit: ", then3.strftime("%H:%M:%S"))
            s13 = now.strftime("%H:%M:%S")
            s23 = then3.strftime("%H:%M:%S")
            FMT = '%H:%M:%S'
            tdelta3 = datetime.strptime(s23, FMT) - datetime.strptime(s13, FMT)
            print("3. Zeitabschnitt: ", tdelta3)

            global g
            g = str(tdelta3)
            b = '", "Checkpoint 1": "'
            c = '", "Checkpoint 2": "'
            f = '", "Checkpoint 3": "'
            h = '", "Checkpoint 4": "0", "Checkpoint 5": "0", "Ziel": "0"}}'
            a = '":{"Start": "'
            y = self.root.ids.team_name.text
            x = '{"'

            name = (x + y + a + z + b + d + c + e + f + g + h)

            to_database = json.loads(name)
            requests.patch(url=self.url, json=to_database)  # z = Startzeit // d = Check1 // e = Check2 // g = Check3

            result = requests.get("https://testapp-4a3b0.firebaseio.com/" + self.root.ids.team_name.text + ".json")
            data = json.loads(result.content.decode())
            self.root.ids.Check3.text = "Delta Checkpoint 3: " + data.get("Checkpoint 3")
            self.root.ids.Check4.text = "Delta Checkpoint 4: "
            self.root.ids.Check5.text = "Delta Checkpoint 5: "
            self.root.ids.Ziel.text = "Delta Ziel: "

            toast("Zeit: " + data.get("Checkpoint 3"))

        elif input == "23475641" and 4 not in _keys and 3 in _keys:
            _keys.append(4)
            then4 = datetime.now()
            print("4. Checkpoint-Zeit: ", then4.strftime("%H:%M:%S"))
            s14 = now.strftime("%H:%M:%S")
            s24 = then4.strftime("%H:%M:%S")
            FMT = '%H:%M:%S'
            tdelta4 = datetime.strptime(s24, FMT) - datetime.strptime(s14, FMT)
            print("4. Zeitabschnitt: ", tdelta4)

            global i
            i = str(tdelta4)
            b = '", "Checkpoint 1": "'
            c = '", "Checkpoint 2": "'
            f = '", "Checkpoint 3": "'
            h = '", "Checkpoint 4": "'
            j = '", "Checkpoint 5": "0", "Ziel": "0"}}'
            a = '":{"Start": "'
            y = self.root.ids.team_name.text
            x = '{"'

            name = (x + y + a + z + b + d + c + e + f + g + h + i + j)

            to_database = json.loads(name)
            requests.patch(url=self.url,
                           json=to_database)  # z = Startzeit // d = Check1 // e = Check2 // g = Check3 // i = Check4

            result = requests.get("https://testapp-4a3b0.firebaseio.com/" + self.root.ids.team_name.text + ".json")
            data = json.loads(result.content.decode())
            self.root.ids.Check4.text = "Delta Checkpoint 4: " + data.get("Checkpoint 4")
            self.root.ids.Check5.text = "Delta Checkpoint 5: "
            self.root.ids.Ziel.text = "Delta Ziel: "

            toast("Zeit: " + data.get("Checkpoint 4"))

        elif input == "91175234" and 5 not in _keys and 4 in _keys:
            _keys.append(5)
            then5 = datetime.now()
            print("5. Checkpoint-Zeit: ", then5.strftime("%H:%M:%S"))
            s15 = now.strftime("%H:%M:%S")
            s25 = then5.strftime("%H:%M:%S")
            FMT = '%H:%M:%S'
            tdelta5 = datetime.strptime(s25, FMT) - datetime.strptime(s15, FMT)
            print("5. Zeitabschnitt: ", tdelta5)

            global k
            k = str(tdelta5)
            b = '", "Checkpoint 1": "'
            c = '", "Checkpoint 2": "'
            f = '", "Checkpoint 3": "'
            h = '", "Checkpoint 4": "'
            j = '", "Checkpoint 5": "'
            l = '", "Ziel": "0"}}'
            a = '":{"Start": "'
            y = self.root.ids.team_name.text
            x = '{"'

            name = (x + y + a + z + b + d + c + e + f + g + h + i + j + k + l)

            to_database = json.loads(name)
            requests.patch(url=self.url,
                           json=to_database)  # z = Startzeit // d = Check1 // e = Check2 // g = Check3 // i = Check4 // k = Check5

            result = requests.get("https://testapp-4a3b0.firebaseio.com/" + self.root.ids.team_name.text + ".json")
            data = json.loads(result.content.decode())
            self.root.ids.Check5.text = "Delta Checkpoint 5: " + data.get("Checkpoint 5")
            self.root.ids.Ziel.text = "Delta Ziel: "

            toast("Zeit: " + data.get("Checkpoint 5"))

        elif input == "99993451" and 6 not in _keys and 5 in _keys:
            _keys.append(6)
            then6 = datetime.now()
            print("6. Checkpoint-Zeit: ", then6.strftime("%H:%M:%S"))
            s16 = now.strftime("%H:%M:%S")
            s26 = then6.strftime("%H:%M:%S")
            FMT = '%H:%M:%S'
            tdelta6 = datetime.strptime(s26, FMT) - datetime.strptime(s16, FMT)
            print("6. Zeitabschnitt: ", tdelta6)

            global m
            m = str(tdelta6)
            b = '", "Checkpoint 1": "'
            c = '", "Checkpoint 2": "'
            f = '", "Checkpoint 3": "'
            h = '", "Checkpoint 4": "'
            j = '", "Checkpoint 5": "'
            l = '", "Ziel": "'
            n = '"}}'
            a = '":{"Start": "'
            y = self.root.ids.team_name.text
            x = '{"'

            name = (x + y + a + z + b + d + c + e + f + g + h + i + j + k + l + m + n)

            to_database = json.loads(name)
            requests.patch(url=self.url,
                           json=to_database)  # z = Startzeit // d = Check1 // e = Check2 // g = Check3 // i = Check4 // k = Check5 // m = Ziel

            result = requests.get("https://testapp-4a3b0.firebaseio.com/" + self.root.ids.team_name.text + ".json")
            data = json.loads(result.content.decode())
            self.root.ids.Ziel.text = "Delta Ziel: " + data.get("Ziel")

            toast("Zeit: " + data.get("Ziel"))

        else:
            toast("Ungültiger Checkpoint")
            print("Fehler")

    theme_cls = ThemeManager()
    theme_cls.primary_palette = 'Blue'
    theme_cls.accent_palette = 'Red'
    theme_cls.theme_style = 'Light'


MainApp().run()
