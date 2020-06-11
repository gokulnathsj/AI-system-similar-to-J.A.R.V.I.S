import pyttsx3
import datetime
import calendar 
import time
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib


# Activating the engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# Time 
hour = int(datetime.datetime.now().hour)
minute = int(datetime.datetime.now().minute)
current_time = "Current time in India is " + str(minute) + " minutes past " + str(hour)  

# Speak Function
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# date Function
def findDay(date): 
    date = datetime.datetime.strptime(date, '%d %m %Y').weekday() 
    return (calendar.day_name[date]) 

# Speaks out Current Time
def Current_time_India(time, week_day):   
    speak(str(datetime.datetime.now().day) + week_day)
    speak(current_time)

# Wishes Mes 
def wishMe():

    date = " ".join(str(datetime.datetime.now()).split(" ")[0].split("-")[::-1])
    week_day = findDay(date)
    
    speak("Activating Hello. Please wait a second")
    time.sleep(1.5)
    speak("Hello Activated")
    time.sleep(1)

    if hour >= 0 and hour < 12:
        speak("Good Morning Gokul")
    
    elif hour >= 12 and hour <= 17:
        speak("Good Afternoon Gokul")
    
    else:
        speak("Good Evening Gokul")

    Current_time_India(current_time, week_day)

# converts the speech to text
def takeCommand():
    recog = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        recog.pause_threshold = 1
        audio = recog.listen(source)
    
    try:
        print("Recognizing...")
        query = recog.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("Say that again please")
        return "None"

    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('gokulnathsj@gmail.com', 'Gokulnathsj@20')
    server.sendmail('gokulnathsj@gmail.com', 'gokulnathsj@gmail.com', content)
    server.close()

if __name__ == "__main__":
    wishMe()

    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak("Searching in Wikipedia..............")
            query = query.replace("wikipedia", " ")
            results = wikipedia.summary(query, sentences=2)
            speak(results)

        elif 'open google' in query:
            webbrowser.open('google.com')

        elif 'play music' in query:
            music_dir = "D:\\"
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, song[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
        
        elif  'who are you' in query:
            speak("I am a A I assistant named HELLO. I am created by Gokul Nath S J, 2nd year Btech Electrical Engineering Student from IIT Palakkad")

        elif 'email to' in query:
            try:
                speak("What Should I send?")
                content = takeCommand()
                to = 'gokulnathsj@gmail.com'
                sendEmail(to, content)
                speak("Email has be sent!")
            
            except Exception as e:
                print(e)
                speak("Sorry Gokul. Email sending failed")
        
        elif 'hello terminate' in query:
            speak("Bye Gokul! We can see Later")
            break

        
