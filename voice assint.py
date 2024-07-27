import sounddevice as sd
import numpy as np
import speech_recognition as sr
from datetime import datetime
import requests
import os

# Initialize the recognizer
recognizer = sr.Recognizer()

def speak(text):
    os.system(f'say "{text}"')

def recognize_speech():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            print("Recognizing...")
            command = recognizer.recognize_google(audio)
            print(f"User said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            speak("Sorry, I did not understand that.")
            return None
        except sr.RequestError:
            speak("Sorry, my speech service is down.")
            return None

def get_time():
    now = datetime.now()
    return now.strftime("%H:%M")

def get_date():
    today = datetime.today()
    return today.strftime("%B %d, %Y")

def search_web(query):
    url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
    response = requests.get(url)
    if response.status_code == 200:
        return f"Here are the search results for {query}"
    else:
        return "Sorry, I couldn't perform the search."

def main():
    speak("Hello! How can I assist you today?")
    while True:
        command = recognize_speech()
        if command:
            if "hello" in command:
                speak("Hello! How can I help you?")
            elif "time" in command:
                current_time = get_time()
                speak(f"The current time is {current_time}")
            elif "date" in command:
                current_date = get_date()
                speak(f"Today's date is {current_date}")
            elif "search" in command:
                query = command.replace("search", "").strip()
                results = search_web(query)
                speak(results)
            elif "stop" in command or "exit" in command:
                speak("Goodbye!")
                break
            else:
                speak("Sorry, I don't understand that command.")

if __name__ == "__main__":
    main()









