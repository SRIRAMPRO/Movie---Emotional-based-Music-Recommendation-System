'''import speech_recognition as sr
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


def play_song(command):
    song = command.replace('play', '')
    if song:
        talk(f'Playing {song}')
        pywhatkit.playonyt(song)
    exit(0)

def greet():
    talk("Hello, what can I do for you?")


def thank_you_response():
    talk("You're welcome.")
    exit(0)

def stop_response():
    talk("okay sir")
    exit(0)

def open_youtube():
    talk("Here you go to Youtube")
    webbrowser.open("youtube.com")


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


def creator_response():
    talk("I was created by Sriram")

def search(command):
    command = command.replace('search', "").lower()
    webbrowser.open(command)

def unknown_command_response():
    print("I didn't understand that. Please say it again.")

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
       
        elif 'who' in command:
            person = command.replace('who', '').strip()
            info = wikipedia.summary(person, 2)
            print(info)
            talk(info)
        
        elif 'thank you' in command:
            thank_you_response()
        elif 'stop' in command or 'exit' in command:
            stop_response()
       
        elif 'open youtube' in command:
            open_youtube()
        elif 'music' in command:
            play_music()
        elif 'how are you' in command:
            how_are_you_response()
        elif 'fine' in command or "good" in command:
            fine_response()
        elif 'what is your name' in command or "what's your name" in command :
            your_name_response()
            
            
        elif 'who create you' in command or 'who made you' in command or 'who is your master' in command:
            creator_response()
        elif 'search' in command:
            search(command)
        elif 'who am i' in command:
            talk("Sorry, I dont know who you are")
        
        else:
            unknown_command_response()'''
import streamlit as st
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser
import os
import time
import smtplib
from ecapture import ecapture as ec
import requests
from bs4 import BeautifulSoup as bs

# Initialize text-to-speech
engine = pyttsx3.init()

st.title("Voice Assistant")

# Streamlit UI
user_command = st.text_input("Enter your command:")

if st.button("Submit"):
    if user_command:
        st.write("Processing...")

        def talk(text):
            st.write(text)
            engine.say(text)
            engine.runAndWait()

        def play_song(command):
            song = command.replace('play', '')
            if song:
                talk(f'Playing {song}')
                pywhatkit.playonyt(song)

        def greet():
            talk("Hello, what can I do for you?")

        def thank_you_response():
            talk("You're welcome.")

        def stop_response():
            talk("Okay, sir.")

        def open_youtube():
            talk("Here you go to Youtube")
            webbrowser.open("https://www.youtube.com/")

        def how_are_you_response():
            talk("I am fine, thank you.")
            talk("How are you, sir?")

        def fine_response():
            talk("It's good to know that you're fine.")

        def your_name_response():
            talk("My name is Friday, I am the assistant of Sriram.")

        if 'song' in user_command:
            play_song(user_command)
        elif 'hello' in user_command:
            greet()
        elif 'hi' in user_command:
            greet()
        elif 'thank you' in user_command:
            thank_you_response()
        elif 'stop' in user_command or 'exit' in user_command:
            stop_response()
        elif 'open youtube' in user_command:
            open_youtube()
        elif 'how are you' in user_command:
            how_are_you_response()
        elif 'fine' in user_command or "good" in user_command:
            fine_response()
        elif 'what is your name' in user_command or "what's your name" in user_command:
            your_name_response()
        else:
            st.write("I didn't understand that. Please say it again.")

