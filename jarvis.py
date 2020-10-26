import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
#import cv2

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning")
    elif hour>=12 and hour<18:
        speak("good afternoon")
    else:
        speak("good evening")
    speak("i am jarvis please tell me how can help you")

def takeCommand():
    #it take a microphone input from the user and return string output
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Recognizing....")
        quary=r.recognize_google(audio, language='en-in')
        print(f"User said: {quary}\n")

    except Exception as e:
        print(e)
        print("Say that again plaese...")
        return "None"
    return quary

def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',822)
    server.ehlo()
    server.starttls()
    server.login('jitendrakumar89973@gmail.com','guptaji8.')
    server.sendmail('jitendrakumar89973@gmail.com',to,content)
    server.close()



if __name__ ==  "__main__":
    wishMe()
    while True:
        quary=takeCommand().lower()

        #take for executing task a based on quary
        if 'wikipedia' in quary:
            speak("searching wikipedia.....")
            quary=quary.replace('wikipwdia',"")
            results=wikipedia.summary(quary,sentences=2)
            speak("according to wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in quary:
            webbrowser.open("youtube.com")
        elif 'quit' in quary:
            speak("ok sir,have a good day")
            break

        elif 'open google' in quary:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in quary:
            webbrowser.open("stackoverflow.com")


        elif 'play music' in quary:
            music_dir='F:\Sounds'
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
        elif 'the time' in quary:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir,the time is now {strTime}")
            print(strTime)
        elif "open visual studio" in quary:
            codePath="C:\\Users\\jitendra kumar\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif "open command prompt" in quary:
            os.system("start cmd")

        #elif "open camera" in quary:
            #cap=cv2.VideoCapture(0)
            #while True:
                #ret,img=cap.read()
                #cv2.imshow('webcam',img)
                #k=cv2.waitKey(50)
                #if k==27:
                    #break
            #cap.release()
            #cv2.destroyAllWindows()

        elif "open notepad plus plus" in quary:
            nodPath="C:\\Program Files (x86)\\Notepad++\\notepad++.exe"
            os.startfile(nodPath)
        elif 'email to sameer' in quary:
            try:
                speak("what should i say")
                content=takeCommand()
                to="crsamirsmtck@gmail.com"
                sendEmail(to,content)
                speak=("email has been sended")
            except Exception as e:
                print(e)
                speak("sorry jitendra bhai,i am not able to send this email")
            
        
