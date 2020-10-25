import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
import random
from requests import get
import wikipedia
import webbrowser
import pywhatkit as kit
import smtplib


engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voices',voices[0].id)

#text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()
#to convert into text(string)
def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Recognizing....")
        quary=r.recognize_google(audio,language='en-in')
        print(f"user said: {quary}")
    except Exception as e:
        speak("say that again please")
        return "None"
    return quary
#to wish
def wish():
    hour=int(datetime.datetime.now().hour)
    if hour<=0 and hour<=12:
        speak("good morning")
    elif hour>=12 and hour<=18:
        speak("good afternoon")
    else:
        speak("good evening") 
    speak("hello sir,i am jarvis please tell me how can help you")

def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('jitendrakumar89973@gmail.com','guptaji8.')
    server.sendmail('jitendrakumar89973@gmail.com',to,content)
    server.close()

if __name__ == "__main__":
    #speak("Hello sir")
    wish()
    while True:

        quary=takecommand().lower()

        #Logid building for task
        if "open notepad" in quary:
            npath="C:\\WINDOWS\\system32\\notepad.exe"
            os.startfile(npath)
        elif "quit" in quary:
            speak("ok sir,have a good day")
            break
        elif "open command prompt" in quary:
            os.system('start cmd')
        elif "open camera" in quary:
            cap=cv2.VideoCapture(0)
            while True:
                ret,img=cap.read()
                cv2.imshow('webcam',img)
                k=cv2.waitKey(58)
                if k==27:
                    break
            cap.release()
            cv2.destroyAllWindows()

        elif "play music" in quary:
            music_dir="F:\Sounds"
            songs=os.listdir(music_dir)
            for song in songs:
                if song.endswith('.mp3'):
            #rd=random.choice(songs)
                    os.startfile(os.path.join(music_dir, song))

        elif "ip address" in quary:
            ip=get('https://api.ipify.org').text
            speak(f"your ip address is {ip}")

        elif "wikipedia" in quary:
            speak("Searching wikipedia....")
            quary=quary.replace("wikipedia","")
            results=wikipedia.summary(quary,sentences=2)
            speak("according to wikipedia")
            speak(results)
            print(results)

        elif "open youtube" in quary:
            webbrowser.open("youtube.com")

        elif "open facebook" in quary:
            webbrowser.open("facebook.com")

        elif "open google" in quary:
            speak("Sir,what should i search on google")
            cm=takecommand().lower()
            webbrowser.open(f"{cm}")
        
        elif "open stack overflow" in quary:
            webbrowser.open("stackoverflow.com")

        elif "send messagr" in quary:
            kit.sendwhatmsg("+918271157125","i am jarvis,this is testing protocol sammir",2,25)

        elif "play songs on youtube" in quary:
            speak("sir,what want you songs")
            mp=takecommand().lower()
            kit.playonyt(f"{mp}")

        elif 'the time' in quary:
            
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir,the time is now {strTime}")
            print(strTime)

        elif "email to sameer" in quary:
            try:
                speak("what should i say?")
                content=takecommand().lower()
                to="crsamirsmtck@gmail.com"
                sendEmail(to,content)
                speak("Email has been sended")
            except Exception as e:
                print(e)
                speak("sorry sir,i am not able to send this email")

        elif "open users" in quary:
            upath="C:\\Users\\jitendra kumar"
            os.startfile(upath)
        elif "open c drive" in quary:
            cpath="C:\\"
            os.startfile(cpath)
        elif "open f drive" in quary:
            fpath="F:\\"
            os.startfile(fpath)
        elif "open music file" in quary:
            mpath="F:\\Sounds"
            os.startfile(mpath)

        elif "open java file" in quary:
            jpath="C:\\Users\\jitendra kumar\\Desktop\\JAVA"
            os.startfile(jpath)
        






