import os
import time
import playsound
import speech_recognition as sr
from gtts import gTTS
import wikipedia
from datetime import datetime

now = datetime.now()
r = sr.Recognizer()

def speak(text):
    tts = gTTS(text=text, lang='vi')
    filename = "voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)

while True:
    with sr.Microphone() as mic:
        audio_data = r.record(mic, duration=5)
        print("Ai: I'm listening....")
        try:
            text = r.recognize_google(audio_data, language="vi-VN")
        except:
            text = ""
        print(text)

        if text == "":
            ai_brain = "Tôi không nghe bạn nói gì"
            speak(ai_brain)
            print(ai_brain)
        elif "xin chào" in text:
            ai_brain = "chào bạn"
            speak(ai_brain)
            print(ai_brain)
        elif "name" in text:
            ai_brain = "my name is siri"
            speak(ai_brain)
            print(ai_brain)
        elif "day" in text:
            ai_brain = now.strftime("%D %m %Y")
            speak(ai_brain)
            print(ai_brain)
        elif "time" in text:
            ai_brain = now.strftime("%H hours %M minutes %S seconds")
            speak(ai_brain)
            print(ai_brain)
        elif text:
            wikipedia.set_lang("vi")
            ai_brain = wikipedia.summary(text, sentences=1)
            speak(ai_brain)
            print(ai_brain)
        elif "bye" in text:
            ai_brain = "see you again"
            speak(ai_brain)
            print(ai_brain)
            break
        else:
            ai_brain = "tôi có thể giúp gì bạn"
            speak(ai_brain)
