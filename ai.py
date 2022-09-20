import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import time
import subprocess
import wolframalpha
import json
import requests
from gtts import gTTS
import playsound


with open('boi_toan_nam.json', encoding="utf-8") as file:
    data= json.load(file)

def speak(text):
    tts = gTTS(text=text, lang='vi')
    filename = "voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)


def wishMe():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("chào buổi sáng")
        print("chào buổi sáng")
    elif hour>=12 and hour<18:
        speak("chào buổi chiều")
        print("chào buổi chiều")
    else:
        speak("chào buổi tối")
        print("chào buổi tối")


def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print(" đang nghe...")
        audio=r.record(source, duration=5)

        try:
            statement=r.recognize_google(audio,language='vi-vn')
            print(f"user said:{statement}\n")
        except:
            speak("bạn nói lại giúp mình với")
            return "None"
        return statement
        
wishMe()
speak("mình là đức bo, mình giúp gì được cho bạn")


if __name__=='__main__':

     while True:
        statement = takeCommand().lower()
        if statement==0:
            continue

        if "tạm biệt" in statement or "ok bye" in statement or "dừng" in statement:
            speak('chương trình sẽ dừng hẵn bye bạn')
            print('chương trình sẽ dừng hẵn bye bạn')
            break

        if 'xin chào' in statement:
            speak('xin chào bạn')

        elif  'wikipedia' in statement:
                statement =statement.replace("wikipedia", " ")
                wikipedia.set_lang("vi")
                result = wikipedia.summary(statement, sentences=2)
                print(result)
                speak(result)

        elif 'mở youtube' in statement:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("youtube is open now")
            time.sleep(5)

        elif 'mở google' in statement:
            webbrowser.open_new_tab("https://www.google.com")
            speak("Google chrome is open now")
            time.sleep(5)

        elif 'mở gmail' in statement:
            webbrowser.open_new_tab("gmail.com")
            speak("Google Mail open now")
            time.sleep(5)

        elif 'thời tiết' in statement:
            api_key="c56d1b9dbe3c2fd720fc0bad4b0a6020"
            base_url="https://api.openweathermap.org/data/2.5/weather?"
            speak("thành phố của bạn là gì")
            print("thành phố của bạn là gì")
            city_name=takeCommand()
            complete_url=base_url+"appid="+api_key+"&q="+city_name
            response = requests.get(complete_url)
            x=response.json()
            if x["cod"]!="404":
                y=x['main']
                current_temperature = y["temp"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                speak(" Nhiệt độ tính theo đơn vị kelvin là " +
                      str(current_temperature) +
                      "\n độ ẩm tính bằng phần trăm là " +
                      str(current_humidiy) +
                      "\n description  " +
                      str(weather_description))
                print(" Nhiệt độ tính bằng đơn vị kelvin = " +
                      str(current_temperature) +
                      "\n độ ẩm (tính bằng phần trăm) = " +
                      str(current_humidiy) +
                      "\n description = " +
                      str(weather_description))

            else:
                speak("không tìm thấy thành phố của bạn ")



        elif 'giờ' in statement:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"bây giờ là {strTime}")

        elif 'bạn là ai' in statement or 'bạn có thể làm gì' in statement:
            speak('tôi là ai do bé lê văn đạt tao ra có thể trả lời cho bạn mọi thứ')


        elif 'mở stackoverflow' in statement:
            webbrowser.open_new_tab("https://stackoverflow.com/login")
            speak("Here is stackoverflow")

        elif 'tin tức' in statement:
            news = webbrowser.open_new_tab("https://www.tinmoi.vn/tin-tuc")
            speak('đây là một số thông mới trong ngày')
            time.sleep(6)


        elif 'tìm'  in statement:
            statement = statement.replace("tìm", "")
            webbrowser.open_new_tab(statement)
            time.sleep(5)

        elif 'hỏi' in statement:
            speak('tôi có thể giúp bạn trả lời gì')
            question=takeCommand()
            app_id="LRQP6W-6KLHAQWW46"
            client = wolframalpha.Client('LRQP6W-6KLHAQWW46')
            res = client.query(question)
            answer = next(res.results).text
            speak(answer)
            print(answer)
        
        elif 'bói' in statement:
            speak('bạn sinh năm bao nhiêu') 
            print('bạn sinh năm bao nhiêu')
            nam_sinh =takeCommand()   
            for p in data['boi_toan_nam']:               
                if p['nam_sinh'] == nam_sinh:
                    if p['mạng'] is not None:
                        speak(p['mạng'])
                        print('mạng: ' + p['mạng'])
                    if p['sao'] is not None:
                        speak(p['sao'])
                        print('sao: ' + p['sao'])
                    if p['hạn'] is not None:
                        speak(p['hạn'])
                        print('hạn: ' + p['hạn'])

        elif "kết thúc" in statement:
            speak("cút")
            subprocess.call(["shutdown", "/l"])

time.sleep(3)

