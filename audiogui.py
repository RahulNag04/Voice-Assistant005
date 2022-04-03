from VideoGui01 import Ui_Virtual_AssistantUI
from PyQt5 import QtCore,QtWidgets,QtGui
from PyQt5.QtGui import QMovie
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtCore import QDate , QTime , QTimer , Qt
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
from pywikihow import WikiHow , search_wikihow
from bs4 import BeautifulSoup
from selenium_web import *
from YT_auto import *
from googlesearch import search
import wolframalpha
import pyautogui
#import randfacts


engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
engine.setProperty('rate',150)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wish():
    hour = int(datetime.datetime.now().hour)
    today_date=datetime.datetime.now()
    
    
    if hour>=0 and hour <12:
        print("Hello Sir, Good morning My Name is Bella.")
        speak(f"Hello Sir, Good morning My Name is Bella.")
        print("Today is " + today_date.strftime("%d") + " of " + today_date.strftime("%B") + " " + today_date.strftime("%Y") + ", And its currently " + (today_date.strftime("%I:")) + (today_date.strftime("%M")) + (today_date.strftime(" %p")))
        speak("Today is " + today_date.strftime("%d") + " of " + today_date.strftime("%B") + " " + today_date.strftime("%Y") + ", And its currently " + (today_date.strftime("%I")) + (today_date.strftime("%M")) + (today_date.strftime("%p")))
        print("what can i do for you sir?")
        speak("what can i do for you sir?")
    elif hour>=12 and hour<16:
        print("Hello Sir, Good Afternoon My Name is Bella.")
        speak(f"Hello Sir, Good Afternoon My Name is Bella.")
        print("Today is " + today_date.strftime("%d") + " of " + today_date.strftime("%B") + " " + today_date.strftime("%Y") + ", And its currently " + (today_date.strftime("%I:")) + (today_date.strftime("%M")) + (today_date.strftime(" %p")))
        speak("Today is " + today_date.strftime("%d") + " of " + today_date.strftime("%B") + " " + today_date.strftime("%Y") + ", And its currently " + (today_date.strftime("%I")) + (today_date.strftime("%M")) + (today_date.strftime("%p")))
        print("what can i do for you sir?")
        speak("what can i do for you sir?")
    else:
        print("Hello Sir, Good Evening My Name is Bella.")
        speak(f"Hello Sir, Good Evening My Name is Bella.")
        print("Today is " + today_date.strftime("%d") + " of " + today_date.strftime("%B") + " " + today_date.strftime("%Y") + ", And its currently " + (today_date.strftime("%I:")) + (today_date.strftime("%M")) + (today_date.strftime(" %p")))
        speak("Today is " + today_date.strftime("%d") + " of " + today_date.strftime("%B") + " " + today_date.strftime("%Y") + ", And its currently " + (today_date.strftime("%I")) + (today_date.strftime("%M")) + (today_date.strftime("%p")))
        print("what can i do for you sir?")
        speak("what can i do for you sir?")

def STT():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.energy_threshold = 10000
            r.adjust_for_ambient_noise(source)
            print(">> Listening........... ")
            
            audio = r.listen(source)
        try:
            print(">> Recognition......... ")
            text = r.recognize_google(audio,language='en-in')
            print(f"Your Command :  {text}\n")
        except Exception:
            print("Sorry Sir Speak Again")
            speak("Sorry Sir Speak Again")
            return "None"
        text = text.lower()
        return text

def screenshot():
        print("Ok Sir , What Should I Name That File ?")
        speak("Ok Sir , What Should I Name That File ?")
        path = STT()
        path1name = path + ".png"
        path1 = "D:\\Python Projects\\Voice03\\Screenshots\\"+ path1name
        kk = pyautogui.screenshot()
        kk.save(path1)
        os.startfile("D:\\Python Projects\\Voice03\\Screenshots\\")
        print("Here Is Your ScreenShot")
        speak("Here Is Your ScreenShot")




class MainThread(QThread):
    def __init__(self):
        super(MainThread,self).__init__()
    
    def run(self):
        self.Task()
        
    
    def STT(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.energy_threshold = 10000
            r.adjust_for_ambient_noise(source)
            print(">> Listening........... ")
            
            audio = r.listen(source)
        try:
            print(">> Recognition......... ")
            text = r.recognize_google(audio,language='en-in')
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
            if 'hello' in self.query:
                print("Hello Sir, My Name is Bella")
                speak("Hello Sir, My Name is Bella")
                print("How May I Help You?")
                speak("How May I Help You?")

            elif 'fine' in self.query:
                print("It's good to know that your fine")
                speak("It's good to know that your fine")

            elif 'what is your name' in self.query:
                print("My name is Bella Sir")
                speak("My name is Bella Sir")

            elif 'what is my name' in self.query:
                print("your name is Rahul Sir")
                speak("your name is Rahul Sir")

            elif 'how are you' in self.query:
                print("I am fine, Thank you")
                speak("I am fine, Thank you")
                print("How are you, Sir")
                speak("How are you, Sir")
                
            elif 'the time' in self.query:
                time = datetime.datetime.now().strftime("%I%M%p")
                print(time)
                speak(time)

            elif 'date' in self.query:
                date = datetime.datetime.now().strftime("%B %d %y")
                print(date)
                speak(date)

            elif 'tell me joke' in self.query:
                get = pyjokes.get_joke()
                print(get)
                speak(get)

            #elif "fact" or "facts" or "tell me fact" in self.query:
                #x = randfacts.getFact()
                #print(x)
                #speak("Did you Know that, "+x)

            elif 'open google' in self.query:
                webbrowser.open('https://www.google.co.in')
                speak("opening google Sir")

            elif 'open youtube' in self.query:
                webbrowser.open("www.youtube.com")
                speak("opening youtube Sir")

            elif 'open wikipedia' in self.query:
                webbrowser.open("https://en.wikipedia.org/wiki/Main_Page")
                speak("opening wikipedia Sir")

            elif 'open facebook' in self.query:
                webbrowser.open("https://www.facebook.com")
                speak("opening facebook Sir")

            elif 'play music' in self.query:
                speak("playing music from pc Sir")
                self.music_dir ="D:\\Python Projects\\Voice03\\Music\\"
                self.musics = os.listdir(self.music_dir)
                os.startfile(os.path.join(self.music_dir,self.musics[0]))

            elif "open word" in self.query:
                print("Opening Microsoft Word")
                speak("Opening Microsoft Word")
                os.startfile("C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE")
                
  
            elif "open excel" in self.query:
                print("Opening Microsoft Excel")
                speak("Opening Microsoft Excel")
                os.startfile("C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE")
                

            elif 'how to' in self.query:
                speak("Getting Data From The Internet !")
                op = self.query.replace("Bella","")
                max_result = 1
                how_to_func = search_wikihow(op,max_result)
                assert len(how_to_func) == 1
                how_to_func[0].print()
                speak(how_to_func[0].summary)

            elif 'temperature in delhi' in self.query:
                search = "temperature in delhi"
                url = f"https://www.google.com/search?q={search}"
                r = requests.get(url)
                data = BeautifulSoup(r.text,"html.parser")
                temp = data.find("div",class_="BNeawe").text
                speak(f"The current {search} is {temp}")

            elif 'temperature in mumbai' in self.query:
                search = "temperature in mumbai"
                url = f"https://www.google.com/search?q={search}"
                r = requests.get(url)
                data = BeautifulSoup(r.text,"html.parser")
                temp = data.find("div",class_="BNeawe").text
                speak(f"The current {search} is {temp}")

            elif 'temperature in greater noida' in self.query:
                search = "temperature in greater noida"
                url = f"https://www.google.com/search?q={search}"
                r = requests.get(url)
                data = BeautifulSoup(r.text,"html.parser")
                temp = data.find("div",class_="BNeawe").text
                speak(f"The current {search} is {temp}")

            elif 'temperature in ghaziabad' in self.query:
                search = "temperature in ghaziabad"
                url = f"https://www.google.com/search?q={search}"
                r = requests.get(url)
                data = BeautifulSoup(r.text,"html.parser")
                temp = data.find("div",class_="BNeawe").text
                speak(f"The current {search} is {temp}")

            elif 'temperature in kolkata' in self.query:
                search = "temperature in kolkata"
                url = f"https://www.google.com/search?q={search}"
                r = requests.get(url)
                data = BeautifulSoup(r.text,"html.parser")
                temp = data.find("div",class_="BNeawe").text
                speak(f"The current {search} is {temp}")

            elif 'temperature in new york' in self.query:
                search = "temperature in new york"
                url = f"https://www.google.com/search?q={search}"
                r = requests.get(url)
                data = BeautifulSoup(r.text,"html.parser")
                temp = data.find("div",class_="BNeawe").text
                speak(f"The current {search} is {temp}")

            elif 'temperature in tokyo' in self.query:
                search = "temperature in tokyo"
                url = f"https://www.google.com/search?q={search}"
                r = requests.get(url)
                data = BeautifulSoup(r.text,"html.parser")
                temp = data.find("div",class_="BNeawe").text
                speak(f"The current {search} is {temp}")

            elif 'temperature in bhopal' in self.query:
                search = "temperature in bhopal"
                url = f"https://www.google.com/search?q={search}"
                r = requests.get(url)
                data = BeautifulSoup(r.text,"html.parser")
                temp = data.find("div",class_="BNeawe").text
                speak(f"The current {search} is {temp}")

            elif 'temperature in nagpur' in self.query:
                search = "temperature in nagpur"
                url = f"https://www.google.com/search?q={search}"
                r = requests.get(url)
                data = BeautifulSoup(r.text,"html.parser")
                temp = data.find("div",class_="BNeawe").text
                speak(f"The current {search} is {temp}")

            elif 'information' in self.query:
                print("you need information related to which topic?")
                speak("you need information related to which topic?")

                r = sr.Recognizer()
                with sr.Microphone() as source:
                    r.energy_threshold = 10000
                    r.adjust_for_ambient_noise(source)
                    print(">> Listening.....")
                    audio = r.listen(source)
                    infor = r.recognize_google(audio)
                    print("searching {} in wikipedia".format(infor))
                    speak("searching {} in wikipedia".format(infor))
                    assist = infow()
                    assist.get_info(infor)

            elif "play" and "video" in self.query:
                print("you want me to play which video?")
                speak("you want me to play which video?")

                r = sr.Recognizer()
                with sr.Microphone() as source:
                    r.energy_threshold = 10000
                    r.adjust_for_ambient_noise(source)
                    print(">> Listening.....")
                    audio = r.listen(source)
                    vid = r.recognize_google(audio)
                    print("Playing {} on youtube".format(vid))
                    speak("Playing {} on youtube".format(vid))
                    assist = music() 
                    assist.play(vid)

            elif 'open map' in self.query:
                webbrowser.open('https://www.google.com/maps/@28.645506,77.3193728,15z//')
                speak("opening map")

            elif 'youtube search' in self.query:
                print("OK SIR , This Is What I found For Your Youtube Search!")
                speak("OK SIR , This Is What I found For Your Youtube Search!")
                self.query = self.query.replace("Bella","")
                self.query = self.query.replace("youtube search","")
                web = 'https://www.youtube.com/results?search_query=' + self.query
                webbrowser.open(web)
                print("You're youtube search results")
                speak("You're youtube search results") 

            elif 'google search' in self.query:
                print("OK SIR , This Is What I found For Your Google Search!")
                speak("OK SIR , This Is What I found For Your Google Search!")
                self.query = self.query.replace("Bella","")
                self.query = self.query.replace("google search","")
                web = 'https://www.google.com/search?q=' + self.query
                webbrowser.open(web)
                print("You're google search results")
                speak("You're google search results")

            elif 'take a screenshot' in self.query:
                screenshot()

            elif 'repeat my word' in self.query:
                print("Speak Sir!")
                speak("Speak Sir!")
                jj = STT()
                print(f"You Said : {jj}")
                speak(f"You Said : {jj}")

            elif 'good night' in self.query:
                print("Good Night")
                speak("Good Night")
                
            elif 'tata bye bye' in self.query:
                print("Bye Bye Sir")
                speak("Bye Bye Sir")
                sys.exit()
                    






startFunctions = MainThread()

class Gui_Start(QMainWindow):

    def __init__(self):
        super(Gui_Start,self).__init__()
        self.audiogui_ui = Ui_Virtual_AssistantUI()
        self.audiogui_ui.setupUi(self)

        self.audiogui_ui.startbutton.clicked.connect(self.startFunc)
        self.audiogui_ui.exitbutton.clicked.connect(self.close)
        self.audiogui_ui.stopbutton.clicked.connect(self.stop)

    def startFunc(self):

        self.audiogui_ui.movies_gif_01 = QtGui.QMovie("Virtual-Assistant-.gif")
        self.audiogui_ui.gif_01.setMovie(self.audiogui_ui.movies_gif_01)
        self.audiogui_ui.movies_gif_01.start()

        self.audiogui_ui.movies_gif_02 = QtGui.QMovie("circle.gif")
        self.audiogui_ui.gif_02.setMovie(self.audiogui_ui.movies_gif_02)
        self.audiogui_ui.movies_gif_02.start()

        self.audiogui_ui.movies_gif_03 = QtGui.QMovie("animated-television-image-0182.gif")
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

    def close(self):
        close = QtWidgets.QMessageBox.question(self,"QUIT","Are you sure want to stop process?",QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if close == QtWidgets.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def stop(self):
        self.audiogui_ui.stop()
        
        
app = QtWidgets.QApplication(sys.argv)
main = Gui_Start()
main.show()
exit(app.exec_())