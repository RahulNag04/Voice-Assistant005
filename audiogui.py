from VideoGui01 import Ui_Virtual_AssistantUI
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtGui import QMovie
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtCore import QDate, QTime, QTimer, Qt
from PyQt5.uic import loadUiType
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
import pyttsx3
import speech_recognition as sr
import sys
import datetime
import time
import pyaudio
import os
import webbrowser
from bs4 import BeautifulSoup
import playsound
import sounddevice
import pyjokes
import requests
import subprocess
from gtts import gTTS
import pywhatkit
import wikipedia
# from pywikihow import WikiHow, search_wikihow
from bs4 import BeautifulSoup
from selenium_web import *
from YT_auto import *
from googlesearch import search
import wolframalpha
import pyautogui
import json


engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 150)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wish():
    hour = int(datetime.datetime.now().hour)
    today_date = datetime.datetime.now()

    if hour >= 0 and hour < 12:
        print("Hello, Good morning My Name is Bella.")
        speak(f"Hello, Good morning My Name is Bella.")
        print("Today is " + today_date.strftime("%d") + " of " + today_date.strftime("%B") + " " + today_date.strftime("%Y") +
              ", And its currently " + (today_date.strftime("%I:")) + (today_date.strftime("%M")) + (today_date.strftime(" %p")))
        speak("Today is " + today_date.strftime("%d") + " of " + today_date.strftime("%B") + " " + today_date.strftime("%Y") +
              ", And its currently " + (today_date.strftime("%I")) + (today_date.strftime("%M")) + (today_date.strftime("%p")))
        print("what can i do for you sir?")
        speak("what can i do for you sir?")
    elif hour >= 12 and hour < 16:
        print("Hello, Good Afternoon My Name is Bella.")
        speak(f"Hello, Good Afternoon My Name is Bella.")
        print("Today is " + today_date.strftime("%d") + " of " + today_date.strftime("%B") + " " + today_date.strftime("%Y") +
              ", And its currently " + (today_date.strftime("%I:")) + (today_date.strftime("%M")) + (today_date.strftime(" %p")))
        speak("Today is " + today_date.strftime("%d") + " of " + today_date.strftime("%B") + " " + today_date.strftime("%Y") +
              ", And its currently " + (today_date.strftime("%I")) + (today_date.strftime("%M")) + (today_date.strftime("%p")))
        print("what can i do for you sir?")
        speak("what can i do for you sir?")
    else:
        print("Hello, Good Evening My Name is Bella.")
        speak(f"Hello, Good Evening My Name is Bella.")
        print("Today is " + today_date.strftime("%d") + " of " + today_date.strftime("%B") + " " + today_date.strftime("%Y") +
              ", And its currently " + (today_date.strftime("%I:")) + (today_date.strftime("%M")) + (today_date.strftime(" %p")))
        speak("Today is " + today_date.strftime("%d") + " of " + today_date.strftime("%B") + " " + today_date.strftime("%Y") +
              ", And its currently " + (today_date.strftime("%I")) + (today_date.strftime("%M")) + (today_date.strftime("%p")))
        print("what can i do for you sir?")
        speak("what can i do for you sir?")


def STT():
    r = sr.Recognizer()
    with sr.Microphone() as source:

        r.adjust_for_ambient_noise(source)
        print(">> Listening........... ")
        r.pause_threshold = 1

        audio = r.listen(source)
    try:
        print(">> Recognition......... ")
        text = r.recognize_google(audio, language='en-in')
        print(f"Your Command :  {text}\n")
    except Exception:
        print("Sorry Speak Again")
        speak("Sorry Speak Again")
        return "None"
    text = text.lower()
    return text


def screenshot():
    print("Ok , What Should I Name That File ?")
    speak("Ok , What Should I Name That File ?")
    path = STT()
    path1name = path + ".png"
    path1 = "D:\\Python Projects\\Voice03\\Screenshots\\" + path1name
    kk = pyautogui.screenshot()
    kk.save(path1)
    os.startfile("D:\\Python Projects\\Voice03\\Screenshots\\")
    print("Here Is Your ScreenShot")
    speak("Here Is Your ScreenShot")


def tellDay():

    day = datetime.datetime.today().weekday() + 1

    Day_dict = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday',
                4: 'Thursday', 5: 'Friday', 6: 'Saturday',
                7: 'Sunday'}

    if day in Day_dict.keys():
        day_of_the_week = Day_dict[day]
        print(day_of_the_week)
        print("The day is " + day_of_the_week)
        speak("The day is " + day_of_the_week)


class MainThread(QThread):
    def __init__(self):
        super(MainThread, self).__init__()

    def run(self):
        self.Task()

    def STT(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:

            r.adjust_for_ambient_noise(source)
            print(">> Listening........... ")
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print(">> Recognition......... ")
            text = r.recognize_google(audio, language='en-in')
            print(f"Your Command :  {text}\n")
        except Exception:
            print("Sorry Sir Speak Again")
            speak("Sorry Sir Speak Again")
            return "None"
        text = text.lower()
        return text

    def Task(self):
        wish()
        while True:
            self.query = self.STT()
            if "hello" in self.query or "hi" in self.query or "hii" in self.query:
                print("Hello, My Name is Bella")
                speak("Hello, My Name is Bella")
                print("How May I Help You?")
                speak("How May I Help You?")

            elif "fine" in self.query:
                print("It's good to know that your fine")
                speak("It's good to know that your fine")

            elif "good morning" in self.query:
                print("Good Morning")
                speak("Good Morning")

            elif "what is your name" in self.query:
                print("My name is Bella")
                speak("My name is Bella")

            elif "what is my name" in self.query:
                print("your name is Rahul")
                speak("your name is Rahul")

            elif "how are you" in self.query:
                print("I am fine, Thank you")
                speak("I am fine, Thank you")
                print("How are you")
                speak("How are you")

            elif "the time" in self.query:
                time = datetime.datetime.now().strftime("%I%M%p")
                print(time)
                speak(time)

            elif 'date' in self.query:
                date = datetime.datetime.now().strftime("%B %d %y")
                print(date)
                speak(date)

            elif 'day' in self.query:
                tellDay()

            elif "tell me joke" in self.query:
                get = pyjokes.get_joke()
                print(get)
                speak(get)

            elif "chrome" in self.query:
                os.startfile(
                    "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
                print("opening google chrome")
                speak("opening google chrome")

            elif "open google" in self.query:
                webbrowser.open('https://www.google.co.in')
                print("opening google")
                speak("opening google")

            elif "open youtube" in self.query:
                webbrowser.open("www.youtube.com")
                print("opening youtube")
                speak("opening youtube")

            elif "open wikipedia" in self.query:
                webbrowser.open("https://en.wikipedia.org/wiki/Main_Page")
                print("opening wikipedia")
                speak("opening wikipedia")

            elif "open facebook" in self.query:
                webbrowser.open("https://www.facebook.com")
                print("opening facebook")
                speak("opening facebook")

            elif "open instagram" in self.query:
                webbrowser.open("https://www.instagram.com")
                print("opening Instagram")
                speak("opening Instagram")

            elif "open twitter" in self.query:
                webbrowser.open("https://www.twitter.com")
                print("opening Twitter")
                speak("opening Twitter")

            elif "launch" in self.query or "website" in self.query:
                print("Tell Me The Name Of The Website")
                speak("Tell Me The Name Of The Website")
                name = STT()
                web = "https://www." + name + ".com"
                webbrowser.open(web)
                print("Opening Website!")
                Speak("Opening Website!")

            elif "play music" in self.query or "play song" in self.query:
                print("playing music from pc")
                speak("playing music from pc")
                self.music_dir = "D:\\Python Projects\\Voice03\\Music\\"
                self.musics = os.listdir(self.music_dir)
                os.startfile(os.path.join(self.music_dir, self.musics[0]))

            elif "play movie" in self.query or "watch movie" in self.query:
                print("Playing Movie on pc")
                speak("Playing Movie on pc")
                os.startfile(
                    "D:\\Python Projects\\Voice03\\Movie\\Bachhan Pandey.mkv")

            elif "open c m d" in self.query or "command prompt" in self.query:
                print("Opening Command Prompt")
                speak("Opening Command Prompt")
                os.startfile(
                    "C:\\Users\\Rahul\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools\\Command Prompt")

            elif "open notepad" in self.query:
                print("Opening Notepad")
                speak("Opening Notepad")
                os.startfile(
                    "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\Notepad")

            elif "open word" in self.query:
                print("Opening Microsoft Word")
                speak("Opening Microsoft Word")
                os.startfile(
                    "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE")

            elif "open excel" in self.query:
                print("Opening Microsoft Excel")
                speak("Opening Microsoft Excel")
                os.startfile(
                    "C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE")

            elif 'how to' in self.query:
                speak("Getting Data From The Internet !")
                op = self.query.replace("Bella", "")
                max_result = 1
                how_to_func = search_wikihow(op, max_result)
                assert len(how_to_func) == 1
                how_to_func[0].print()
                speak(how_to_func[0].summary)

            # elif 'information' in self.query:
            #     print("you need information related to which topic?")
            #     speak("you need information related to which topic?")

            #     r = sr.Recognizer()
            #     with sr.Microphone() as source:

            #         r.adjust_for_ambient_noise(source)
            #         print(">> Listening.....")
            #         audio = r.listen(source)
            #         infor = r.recognize_google(audio)
            #         print("searching {} in wikipedia".format(infor))
            #         speak("searching {} in wikipedia".format(infor))
            #         assist = infow()
            #         assist.get_info(infor)

            elif "play" and "video" in self.query:
                print("you want me to play which video?")
                speak("you want me to play which video?")

                r = sr.Recognizer()
                with sr.Microphone() as source:

                    r.adjust_for_ambient_noise(source)
                    print(">> Listening.....")
                    audio = r.listen(source)
                    vid = r.recognize_google(audio)
                    print("Playing {} on youtube".format(vid))
                    speak("Playing {} on youtube".format(vid))
                    assist = music()
                    assist.play(vid)

            elif "open map" in self.query:
                webbrowser.open(
                    'https://www.google.com/maps/@28.645506,77.3193728,15z//')
                speak("opening map")

            elif "youtube search" in self.query:
                print("OK , This Is What I found For Your Youtube Search!")
                speak("OK , This Is What I found For Your Youtube Search!")
                self.query = self.query.replace("Bella", "")
                self.query = self.query.replace("youtube search", "")
                web = 'https://www.youtube.com/results?search_query=' + self.query
                webbrowser.open(web)
                print("You're youtube search results")
                speak("You're youtube search results")

            elif "google search" in self.query:
                print("OK , This Is What I found For Your Google Search!")
                speak("OK , This Is What I found For Your Google Search!")
                self.query = self.query.replace("Bella", "")
                self.query = self.query.replace("google search", "")
                web = 'https://www.google.com/search?q=' + self.query
                webbrowser.open(web)
                print("You're google search results")
                speak("You're google search results")

            elif "take a screenshot" in self.query:
                screenshot()

            elif "repeat my word" in self.query:
                print("Speak Sir!")
                speak("Speak Sir!")
                jj = STT()
                print(f"You Said : {jj}")
                speak(f"You Said : {jj}")

            elif "temperature in greater noida" in self.query:
                search = "temperature in greater noida"
                url = f"https://www.google.com/search?q={search}"
                r = requests.get(url)
                data = BeautifulSoup(r.text, "html.parser")
                temp = data.find("div", class_="BNeawe").text
                print(f"Its Current {search} is {temp}")
                speak(f"Its Current {search} is {temp}")

            elif "temperature in delhi" in self.query:
                search = "temperature in delhi"
                url = f"https://www.google.com/search?q={search}"
                r = requests.get(url)
                data = BeautifulSoup(r.text, "html.parser")
                temp = data.find("div", class_="BNeawe").text
                print(f"Its Current {search} is {temp}")
                speak(f"Its Current {search} is {temp}")

            elif "temperature in mumbai" in self.query:
                search = "temperature in mumbai"
                url = f"https://www.google.com/search?q={search}"
                r = requests.get(url)
                data = BeautifulSoup(r.text, "html.parser")
                temp = data.find("div", class_="BNeawe").text
                print(f"Its Current {search} is {temp}")
                speak(f"Its Current {search} is {temp}")

            elif "temperature in ghaziabad" in self.query:
                search = "temperature in ghaziabad"
                url = f"https://www.google.com/search?q={search}"
                r = requests.get(url)
                data = BeautifulSoup(r.text, "html.parser")
                temp = data.find("div", class_="BNeawe").text
                print(f"Its Current {search} is {temp}")
                speak(f"Its Current {search} is {temp}")

            elif "temperature in kolkata" in self.query:
                search = "temperature in kolkata"
                url = f"https://www.google.com/search?q={search}"
                r = requests.get(url)
                data = BeautifulSoup(r.text, "html.parser")
                temp = data.find("div", class_="BNeawe").text
                print(f"Its Current {search} is {temp}")
                speak(f"Its Current {search} is {temp}")

            elif "temperature in new york" in self.query:
                search = "temperature in new york"
                url = f"https://www.google.com/search?q={search}"
                r = requests.get(url)
                data = BeautifulSoup(r.text, "html.parser")
                temp = data.find("div", class_="BNeawe").text
                print(f"Its Current {search} is {temp}")
                speak(f"Its Current {search} is {temp}")

            elif "temperature in tokyo" in self.query:
                search = "temperature in tokyo"
                url = f"https://www.google.com/search?q={search}"
                r = requests.get(url)
                data = BeautifulSoup(r.text, "html.parser")
                temp = data.find("div", class_="BNeawe").text
                print(f"Its Current {search} is {temp}")
                speak(f"Its Current {search} is {temp}")

            elif "temperature in bhopal" in self.query:
                search = "temperature in bhopal"
                url = f"https://www.google.com/search?q={search}"
                r = requests.get(url)
                data = BeautifulSoup(r.text, "html.parser")
                temp = data.find("div", class_="BNeawe").text
                print(f"Its Current {search} is {temp}")
                speak(f"Its Current {search} is {temp}")

            elif "temperature in nagpur" in self.query:
                search = "temperature in nagpur"
                url = f"https://www.google.com/search?q={search}"
                r = requests.get(url)
                data = BeautifulSoup(r.text, "html.parser")
                temp = data.find("div", class_="BNeawe").text
                print(f"Its Current {search} is {temp}")
                speak(f"Its Current {search} is {temp}")

            elif "temperature in lucknow" in self.query:
                search = "temperature in lucknow"
                url = f"https://www.google.com/search?q={search}"
                r = requests.get(url)
                data = BeautifulSoup(r.text, "html.parser")
                temp = data.find("div", class_="BNeawe").text
                print(f"Its Current {search} is {temp}")
                speak(f"Its Current {search} is {temp}")

            elif "temperature in hyderabad" in self.query:
                search = "temperature in hyderabad"
                url = f"https://www.google.com/search?q={search}"
                r = requests.get(url)
                data = BeautifulSoup(r.text, "html.parser")
                temp = data.find("div", class_="BNeawe").text
                print(f"Its Current {search} is {temp}")
                speak(f"Its Current {search} is {temp}")

            elif "temperature in bengaluru" in self.query:
                search = "temperature in bengaluru"
                url = f"https://www.google.com/search?q={search}"
                r = requests.get(url)
                data = BeautifulSoup(r.text, "html.parser")
                temp = data.find("div", class_="BNeawe").text
                print(f"Its Current {search} is {temp}")
                speak(f"Its Current {search} is {temp}")

            elif "temperature in chennai" in self.query:
                search = "temperature in chennai"
                url = f"https://www.google.com/search?q={search}"
                r = requests.get(url)
                data = BeautifulSoup(r.text, "html.parser")
                temp = data.find("div", class_="BNeawe").text
                print(f"Its Current {search} is {temp}")
                speak(f"Its Current {search} is {temp}")

            elif "good evening" in self.query:
                print("Good Evening")
                speak("Good Evening")

            elif "good night" in self.query:
                print("Good Night")
                speak("Good Night")

            elif "quit" in self.query or "bye bye" in self.query or "exit" in self.query:
                print("Bye Bye")
                speak("Bye Bye")
                sys.exit()


startFunctions = MainThread()


class Gui_Start(QMainWindow):

    def __init__(self):
        super(Gui_Start, self).__init__()
        self.audiogui_ui = Ui_Virtual_AssistantUI()
        self.audiogui_ui.setupUi(self)

        self.audiogui_ui.startbutton.clicked.connect(self.startFunc)
        self.audiogui_ui.exitbutton.clicked.connect(self.closeFunc)
        self.audiogui_ui.stopbutton.clicked.connect(self.stopFunc)

    def startFunc(self):

        self.audiogui_ui.movies_gif_01 = QtGui.QMovie("Virtual-Assistant-.gif")
        self.audiogui_ui.gif_01.setMovie(self.audiogui_ui.movies_gif_01)
        self.audiogui_ui.movies_gif_01.start()

        self.audiogui_ui.movies_gif_02 = QtGui.QMovie("circle.gif")
        self.audiogui_ui.gif_02.setMovie(self.audiogui_ui.movies_gif_02)
        self.audiogui_ui.movies_gif_02.start()

        self.audiogui_ui.movies_gif_03 = QtGui.QMovie(
            "animated-television-image-0182.gif")
        self.audiogui_ui.gif_03.setMovie(self.audiogui_ui.movies_gif_03)
        self.audiogui_ui.movies_gif_03.start()

        self.audiogui_ui.movies_gif_04 = QtGui.QMovie("gif05.gif")
        self.audiogui_ui.gif_04.setMovie(self.audiogui_ui.movies_gif_04)
        self.audiogui_ui.movies_gif_04.start()

        self.audiogui_ui.movies_gif_05 = QtGui.QMovie("gifbackground.gif")
        self.audiogui_ui.gif_05.setMovie(self.audiogui_ui.movies_gif_05)
        self.audiogui_ui.movies_gif_05.start()

        timer = QTimer(self)

        timer.timeout.connect(self.showtime)

        timer.start(1000)

        startFunctions.start()

    def showtime(self):

        current_time = QTime.currentTime()

        label_time = current_time.toString("h:mm:ssa")

        time = "Time: " + label_time

        self.audiogui_ui.timetextBrowser.setText(time)

        now = QDate.currentDate()

        label_date = now.toString()

        date = "Date: " + label_date

        self.audiogui_ui.datetextbrowser.setText(date)

    def closeFunc(self):
        close = QMessageBox.question(
            self, "QUIT", "Are you sure want to stop process?", QMessageBox.Yes | QMessageBox.No)
        if close == QMessageBox.Yes:
            print('Window closed')
            sys.exit()

        else:
            pass

    def stopFunc(self):
        startFunctions.terminate()
        time.sleep(10)


app = QtWidgets.QApplication(sys.argv)
main = Gui_Start()
main.show()
sys.exit(app.exec_())
