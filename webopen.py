import json
import speech_recognition as sr
from gtts import gTTS
import playsound
import os


def speak(text):
    tts = gTTS(text=text, lang='vi')
    filename = "voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print(" đang nghe...")
        audio=r.record(source, duration=5)

        try:
            statement=r.recognize_google(audio, language=('vi-vn'))
            print(f"user said:{statement}\n")
        except:
            speak("bạn nói lại giúp mình với")
            return "None"
        return statement
        


with open('data.json', encoding="utf-8") as file:
    data= json.load(file)
    


if __name__=='__main__':
        while True:
            statement = takeCommand().lower()
            if statement==0:
                continue
            if 'hello' in statement:  
                speak('what is your id number')
                print('what is your id number')

                id_number =takeCommand()
                print(id_number)


                for p in data['data']:
                    if p['id_number'] == id_number:
                        if p['name'] is not None:
                            speak(p['name'])
                            print('name: ' + p['name'])
                        if p['birthdate'] is not None:
                            speak(p['birthdate'])
                            print('birthdate: ' + p['birthdate'])

            
