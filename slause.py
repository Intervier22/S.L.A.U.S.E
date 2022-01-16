from sys import addaudithook, modules
import pyttsx3
import pyautogui
import datetime
import wikipedia
import webbrowser as wb
import os
import random
import speech_recognition as sr
import pywhatkit
import webbrowser
#import smtplib
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices)
engine.setProperty('voice',voices[0].id)

# Defining Speak Function
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Defining Greeting FUnction
def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour <12:
        speak("Good Morning Sir!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon Sir!")

    else:
        speak("Good Evening Sir.")

    speak("I am Slause,Sir. Please tell me how may I help you.....")
    print("I am Slause,Sir. Please tell me how may I help you.")

def takeCommand():
    # It take microphone input from user and returns string output
    
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold =1
        audio=r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language="en-in")
        print(f"User Said: {query}\n")
    
    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query

def createTxtFIle():
    speak('Please tell me filename')
    query = takeCommand().lower()
    f = open(str(query)+".txt", "w")
    speak('Please tell me what to write')
    query = takeCommand().lower()
    f.write(str(query))
    f.close()
    speak('File created')
    
if __name__ == "__main__":

    INFO = '''
        
░██████╗██╗░░░░░░█████╗░██╗░░░██╗░██████╗███████╗
██╔════╝██║░░░░░██╔══██╗██║░░░██║██╔════╝██╔════╝
╚█████╗░██║░░░░░███████║██║░░░██║╚█████╗░█████╗░░
░╚═══██╗██║░░░░░██╔══██║██║░░░██║░╚═══██╗██╔══╝░░
██████╔╝███████╗██║░░██║╚██████╔╝██████╔╝███████╗
╚═════╝░╚══════╝╚═╝░░╚═╝░╚═════╝░╚═════╝░╚══════╝
        '''
    print(INFO)

    wishme()
    while True:
        query = takeCommand().lower()
        
        # Logic of executing task based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia....')
            query = query.replace('wikipedia',"")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        
        # Logic to stop program
        elif ('goodbye') in query:                          
            speak('Goodbye Sir , Slause Powering off in 3 2 1')
            quit()

        elif query=='slaus':
            speak("'Yes Sir?', 'What can I doo for you sir?'")

        elif '*' in query:
            speak("You dont have a dic-k.")

        elif ('your name') in query:
            speak("My name is Slaus")
        
        elif ('hello') in query or ('hi') in query:
            speak("Welcome to Slaus Virtual Intelligence project. At you service sir.")
            
        elif ('like google assistant') in query or ('like siri') in query or ('like alexa') in query:
            speak("Never say that again you son of a bitch.")

        elif ('thanks') in query or ('tanks') in query or ('thank you') in query:  
            speak("You are welcome sir, no problem")

        elif 'play youtube' in query:
            webbrowser.open("http://youtube.com", new=1)

        elif 'open intervier github profile' in query:
            webbrowser.open("https://github.com/Intervier22", new=1)

        elif 'open spotify' in query:
            webbrowser.open("open.spotify.com", new=1)
        
        elif 'open gmail' in query:
            webbrowser.open("https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox", new=1)
            
        elif 'open whatsapp' in query:
            webbrowser.open("web.whatsapp.com", new=1)
        
        elif 'open Instagram' in query:
             webbrowser.open('http://instagram.com', new=1)

        elif 'open google' in query:
             webbrowser.open('www.google.com', new=1)
            
        elif 'meet' in query:
            wb.open("meet.google.com",new=1)
            
        elif 'open ndf' or 'my meet' in query:
            webbrowser.open("meet.google.com/ndf-mrve-tdf", new=1)

        elif 'open zaha' in query:
            webbrowser.open("meet.google.com/cge-zaha-wmg", new=1)
        
        elif 'play music' in query:
            # you have to change the music directory
            music_dir = 'D:\\musicplease'
            songs = os.listdir(music_dir)
            # print(songs)
            song=random.choice(songs)
            speak(f"Playing {song}")
            os.startfile(os.path.join(music_dir, song))

        elif 'the time' in query:
            strTime= datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir the time {strTime}")

        elif 'open minecraft' in query:
            tlauncher = 'C:\\Users\\yashr\\AppData\\Roaming\\.minecraft\\TLauncher.exe'
            speak("Opening Minecraft")
            os.startfile(tlauncher)

        elif 'play jingle bells' in query:
            jingle_bells = 'D:\\musicplease\\jingle_bells.mp3'
            os.startfile(jingle_bells)
            
        elif'why are you made' in query:
            print("I m Slause   i m made to help people \n i m made by Intervier22 and Yashthealien14")
            speak("I m Slause   i m made to help people \n i m made by Intervier22 and Yashthealien14")

        elif ('sleep mode') in query:
            speak("good night sir")
            os.system('rundll32.exe powrprof.dll,SetSuspendState 0,1,0')

        elif 'create text file' in query:
         # create text file instantaneously
            speak('creating file....')
            createTxtFIle()
            
        elif "take a screenshot" in query:
            speak("sir, please tell me name for this screenshot file")
            name = takeCommand().lower()
            speak("please hold the screen for few seconds i am taking screenshot")
            time.sleep(2)
            img = pyautogui.screenshot()
            img.save(f"{name}.jpg")
            speak("i am done sir, the screenshot is saved to our main folder now i am ready to take next command")

