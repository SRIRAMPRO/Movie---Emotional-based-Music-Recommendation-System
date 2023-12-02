import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import subprocess
import random
import webbrowser
import os
import ctypes
import time
import smtplib
from ecapture import ecapture as ec
import requests
from bs4 import BeautifulSoup as bs



name = "friday"

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def listen_to_commands():
    try:
        with sr.Microphone() as source:
            print('Listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice).lower()
            command = command.lower()
            if 'friday' in command:
                command = command.replace('friday', '')
            print('Command:', command)
            return command
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand your command. Can you please repeat?")
        return ""
    except sr.RequestError:
        talk("Sorry, there was an issue with the request. Please try again.")
        return ""

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        talk("Good Morning Sir !")
    elif hour >= 12 and hour < 18:
        talk("Good Afternoon Sir !")
    else:
        talk("Good Evening Sir !")
    talk("I am Friday. How can I help you?")

def sendmail():
    talk("Give the email address you want to send the mail")
    mail = listen_to_commands()
    talk("What should I say?")
    text = listen_to_commands()
    sendEmail(mail, text)

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('nothingbusy80@gmail.com', 'sivasriram.7.3.1.')
    server.sendmail('nothingbusy80@gmail.com', to, content)
    server.close()

def play_song(command):
    song = command.replace('play', '')
    if song:
        talk(f'Playing {song}')
        pywhatkit.playonyt(song)
    exit(0)

def greet():
    talk("Hello, what can I do for you?")

def getTime():
    current_time = datetime.datetime.now().strftime('%I:%M %p')
    talk("Current time is " + current_time)

def date_response():
    talk("Sorry, you are single for life.")

def are_you_single():
    talk("No, I have a boy bestie named wifi. Better luck next time")

def tell_joke():
    joke = pyjokes.get_joke()
    talk(joke)

def thank_you_response():
    talk("You're welcome.")
    exit(0)

def stop_response():
    talk("okay sir")
    exit(0)

def open_youtube():
    talk("Here you go to Youtube")
    webbrowser.open("youtube.com")

def open_google():
    talk("Here you go to Google")
    webbrowser.open("google.com")

def open_stackoverflow():
    talk("Here you go to Stack Over flow. Happy coding")
    webbrowser.open("stackoverflow.com")

def play_music():
    talk("Here you go with music")
    music_dir = "E:\SONGS"  
    songs = os.listdir(music_dir)
    if songs:
        random_song = random.choice(songs)
        song_path = os.path.join(music_dir, random_song)
        os.startfile(song_path)
    else:
        talk("No songs found in the music directory.")
    exit(0)

def how_are_you_response():
    talk("I am fine, Thank you")
    talk("How are you, Sir")

def fine_response():
    talk("It's good to know that you're fine")

def your_name_response():
    talk("My name is Friday, I am the assistant of Sriram")

def change_name():
    talk("What would you like to call me?")
    global name
    name = listen_to_commands()
    talk("Thanks for naming me " + name)

def creator_response():
    talk("I was created by Sriram")

def search(command):
    command = command.replace('search', "").lower()
    webbrowser.open(command)

def unknown_command_response():
    print("I didn't understand that. Please say it again.")

def lock_window():
    talk("Locking the device")
    ctypes.windll.user32.LockWorkStation()

def do_nothing():
    talk("For how much time do you want to stop Friday from listening to commands?")
    a = listen_to_commands()
    talk("I am waiting for your command")
    time.sleep(int(a))

def shutdown_system():
    talk("Oops, your system is shutting down")
    subprocess.call('shutdown /p /f')

def where_is(command):
    command = command.replace("where is", "")
    location = command
    talk("Requested location is here")
    webbrowser.open("https://www.google.nl/maps/place/" + location)

def take_photo():
    stamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    photo = f"img_{stamp}.jpg"
    ec.capture(0, "Friday's camera", photo)

    if os.path.isfile(photo):
        os.system(photo)
    else:
        talk("Oops, your image capture failed")
    exit(0)

def relationship_request(command):
    if "will you be my gf" in command or "will you be my bf" in command:
        talk("Yeah sure, I love you")

def love_response():
    talk("I love you too")

def get_news():
    try:
        talk("Here are some headlines from the Times of India")
        headlines = requests.get("https://timesofindia.indiatimes.com/home/headlines")
        if headlines.status_code==200:
            soup=bs(headlines.text,"html.parser")
            news = soup.find_all("div",class_="headline")
            if news:
                talk("here the latest news")
                for i,news in enumerate(news,start=1):
                    if i<=5:
                        talk(f"{i}.{news.text}")
            else:
                talk("Sorry, couldn't find any news")
        else:
            talk("Sorry, couldn't fetch any news")
    except Exception as e:
        talk("An error occured while fetching news headlines")
        print(e)




if __name__ == '__main__':
    wishMe()
    while True:
        command = listen_to_commands()
        if 'song' in command:
            play_song(command)
        elif 'hello' in command:
            greet()
        elif 'hi' in command:
            greet()
        elif 'time' in command:
            getTime()
        elif 'who' in command:
            person = command.replace('who', '').strip()
            info = wikipedia.summary(person, 2)
            print(info)
            talk(info)
        elif 'date' in command:
            date_response()
        elif 'you single' in command:
            are_you_single()
        elif 'joke' in command:
            tell_joke()
        elif 'thank you' in command:
            thank_you_response()
        elif 'stop' in command or 'exit' in command:
            stop_response()
        elif 'send mail' in command:
            sendmail()
        elif 'open youtube' in command:
            open_youtube()
        elif 'open google' in command:
            open_google()
        elif 'open stackoverflow' in command:
            open_stackoverflow()
        elif 'music' in command:
            play_music()
        elif 'how are you' in command:
            how_are_you_response()
        elif 'fine' in command or "good" in command:
            fine_response()
        elif 'what is your name' in command or "what's your name" in command :
            your_name_response()
            
            
        elif 'change your name' in command:
            change_name()
        elif 'who create you' in command or 'who made you' in command or 'who is your master' in command:
            creator_response()
        elif 'search' in command:
            search(command)
        elif 'who am i' in command:
            talk("Sorry, I dont know who you are")
        elif 'lock window' in command:
            lock_window()
        elif "dont do anything" in command or 'stop listening' in command:
            do_nothing()
        elif 'shutdown system' in command:
            shutdown_system()
        elif 'where is' in command:
            where_is(command)
        elif 'take a photo' in command or 'camera' in command:
            take_photo()
        elif "will you be my gf" in command or "will you be my bf" in command:
            relationship_request(command)
        elif 'i love you' in command:
            love_response()
        elif 'news' in command:
            get_news()
        else:
            unknown_command_response()
