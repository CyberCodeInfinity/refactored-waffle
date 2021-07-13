from tkinter.filedialog import *
import pyautogui
import PySimpleGUI as sg
import tkinter as tk
from tkinter import *
from PIL import Image,ImageTk
from datetime import datetime
from tkinter import messagebox, filedialog
from googlesearch import search
import speech_recognition as sr
import tkinter as tk
import requests
import time
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser
import subprocess
import turtle as tl
import cv2
import numpy as np


listener = sr.Recognizer()
engine = pyttsx3.init()


def speak(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'mark' in command:
                command = command.replace('mark', '')
                speak('Yes sir...')
                
    except:
        pass
    return command
 

def run_user_request():
    command = take_command()
    print(command)
    if 'mark' in command:
        speak('Yes sir...')

    def user_query():
        if 'introduce' in command:
            speak("Hi, my name is mark, i am a visual assistant. How can i help you?")

        elif 'what can you do' in command:
            speak("Here's what i can do: ")
            print('Search google')
            print('Open google')
            print('Open youtube')
            print('Search youtube')
            print('Open amazon')
            print('Open google classroom')
            print('Open cmd')
            print('Open calculator')
            print('Open notepad')
            print('What is the time?')

        elif 'open google' in command:
            speak('Opening google...')
            webbrowser.open('https://www.google.com/')

        elif 'search google' in command:
            sr.Microphone(device_index=1)

            r=sr.Recognizer()


            r.energy_threshold=5000

            with sr.Microphone() as source:
                speak("What do you want to search for?")
                audio = r.listen(source)
                try:
                    text = r.recognize_google(audio)
                    find = "Your search : {}".format(text)
                    speak('Searching ' + 'for : {}'.format(text))
                    print(search)
                    url = 'https://www.google.co.in/search?q='
                    search_url = url + text
                    webbrowser.open(search_url)
                except:
                    speak("Sorry, i can't recognize")


        elif 'youtube' in command:
            speak('Opening youtube...')
            webbrowser.open('https://www.youtube.com/')

        elif 'whatsapp' in command:
            speak('Opening whatsapp...')
            webbrowser.open('https://web.whatsapp.com/')

        elif 'pinterest' in command:
            speak('Opening pintrest...')
            webbrowser.open('https://in.pinterest.com/')

        elif 'screenshot' in command:
            speak('Opening screenshot app...')
            subprocess.call('SnippingTool.exe')

        elif 'notepad' in command:
            speak('Opening notepad...')
            subprocess.call('notepad.exe')

        elif 'command prompt' in command:
            speak('Opening command prompt...')
            subprocess.call('cmd.exe')

        elif 'play' in command:
            song = command.replace('play', '')
            speak('playing ' + song)
            pywhatkit.playonyt(song)

        elif 'weather' in command:
            speak('Ok, please type the location of the place in the blank window.')
            def getWeather(canvas):
                city = textField.get()
                api = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=06c921750b9a82d8f5d1294e1586276f"

                # Requests for json data
                json_data = requests.get(api).json()
                condition = json_data['weather'][0]['main']
                temp = int(json_data['main']['temp'] - 273.15)
                min_temp = int(json_data['main']['temp_min'] - 273.15)
                max_temp = int(json_data['main']['temp_max'] - 273.15)
                pressure = json_data['main']['pressure']
                humidity = json_data['main']['humidity']
                wind = json_data['wind']['speed']
                sunrise = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunrise'] - 21600))
                sunset = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunset'] - 21600))
                
                # Getting info and conditions
                final_info = condition + "\n" + str(temp) + "°C" 
                final_data = "\n"+ "Min Temp: " + str(min_temp) + "°C" + "\n" + "Max Temp: " + str(max_temp) + "°C" +"\n" + "Pressure: " + str(pressure) + "\n" +"Humidity: " + str(humidity) + "\n" +"Wind Speed: " + str(wind) + "\n" + "Sunrise: " + sunrise + "\n" + "Sunset: " + sunset
                label1.config(text = final_info)
                label2.config(text = final_data)

                return 'Thank you for using Weather App!'


            # Creating area and perimeter for the window
            canvas = tk.Tk()
            canvas.geometry("600x500")
            canvas.title("Weather App")
            f = ("JetBrains Mono", 15)
            t = ("JetBrains Mono", 20)


            # Adjusting size of the window
            textField = tk.Entry(canvas, justify='center', width=20, font=t)
            textField.pack(pady=20)
            textField.focus()
            textField.bind('<Return>', getWeather)


            # Getting labels and running the app
            label1 = tk.Label(canvas, font=t)
            label1.pack()
            label2 = tk.Label(canvas, font=f)
            label2.pack()
            canvas.mainloop()

        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            speak('The time is ' + time)

        elif 'what' in command:
            person = command.replace('what', '')
            info = wikipedia.summary(person, 1)
            print(info)
            speak(info)

        elif 'who' in command:
            person = command.replace('who', '')
            info = wikipedia.summary(person, 1)
            print(info)
            speak(info)

        elif 'when' in command:
            person = command.replace('when', '')
            info = wikipedia.summary(person, 1)
            print(info)
            speak(info)

        elif 'why' in command:
            person = command.replace('who is', '')
            info = wikipedia.summary(person, 1)
            print(info)
            speak(info)

        elif 'joke' in command:
            speak("Ok here's a joke...")
            speak(pyjokes.get_joke())

        elif 'movies' in command:
            speak('Opening amazon prime movies...')
            webbrowser.open('https://www.primevideo.com/ref=av_auth_return_redir')

        elif 'cartoon photo' in command:
            speak('Sure, why not, just select your file!')
            photo = askopenfilename()
            img = cv2.imread(photo)

            grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            grey = cv2.medianBlur(grey, 5)
            edges = cv2.adaptiveThreshold(grey, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)

            #cartoonize
            color = cv2.bilateralFilter(img, 9, 250, 250)
            cartoon = cv2.bitwise_and(color, color, mask=edges)

            cv2.imshow("Image", img)
            cv2.imshow("Cartoon", cartoon)

            #save
            cv2.imwrite("cartoon.png", cartoon)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

        elif 'camera' in command:
            speak('Opening camera...')
            cap = cv2.VideoCapture(0)

            while True:
                ret, img = cap.read()
                cv2.imshow('Camera App', img)
                wk = cv2.waitKey(10)
                if wk == 27:
                    break

            cap.release()
            cv2.destroyAllWindows()
            

        elif 'close' in command:
            speak('please click on ok')
            quit()
            

        

    user_query()


while True:
    run_user_request()
