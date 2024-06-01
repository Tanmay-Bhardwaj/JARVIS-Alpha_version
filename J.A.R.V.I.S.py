'''

░░░░░██╗░█████╗░██████╗░██╗░░░██╗██╗░██████╗
░░░░░██║██╔══██╗██╔══██╗██║░░░██║██║██╔════╝
░░░░░██║███████║██████╔╝╚██╗░██╔╝██║╚█████╗░
██╗░░██║██╔══██║██╔══██╗░╚████╔╝░██║░╚═══██╗
╚█████╔╝██║░░██║██║░░██║░░╚██╔╝░░██║██████╔╝
░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝╚═════╝░ 
'''
#----------------------------------------Imported packages---------------------------------------------------------------------------
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser
#---------------------------------------Prerequsites to activate JARVIS--------------------------------------------------------------


listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)



def talk(text):
    engine.say(text)
    engine.runAndWait()
    


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'jarvis' in command:
                command = command.replace('jarvis', '')
                print(command)
    except:
        pass
    return command

#-----------------------------------------------------------Enabelling talking with JARVIS--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def introduction():
    talk("I am Jarvis. A virtual, artificial intelligence and I am here to assist you in variety of tasks, as best as I can. twentyfour hours a day, and seven days a week. Importing all preferances from home database and herm interface. Systems, now fully operational.")
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#---------------------------------------------------------Commands to execute--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def run_jarvis():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play',command)
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'who the heck is' in command:
        person = command.replace('who the heck is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'meeting' in command:
        talk("Opening google meet")
        url= 'https://meet.google.com'  
        webbrowser.open_new_tab(url)   
    elif "favourite songs" in command:
        talk("Here you go sir, playing your favourites")
        ytmusic='https://music.youtube.com/watch?v=D5d5xinZI3E&list=PLoQKO7gnb11aH65-CW8WusqKiWHzTqvx_'
        webbrowser.open_new_tab(ytmusic)
    elif "news" in command:
        talk("The latest news is ")
        newslink='https://www.bbc.com/news'
        webbrowser.open_new_tab(newslink)
    elif "whatsapp" in command:
        talk("Opening whatsapp")
        open("WhatsApp")
    elif "kaise" in command:
        talk("Mein. theek. hoon")
    elif "inbox" in command:
        talk("Opening Gmail")
        gmail='https://mail.google.com/mail/u/0/#inbox'
        webbrowser.open_new_tab(gmail)
    elif "hello how r u " in command:
        talk("Hello sir. I am fine how are you ")
    elif "I am Good" in command:
        talk("Nice to hear that.")
    elif "Search" in command:
        talk("Opening browser")
        url_search='https://www.google.com/search?client=opera&q=google&sourceid=opera&ie=UTF-8&oe=UTF-8'
        webbrowser.open_new_tab(url_search)
    elif "get me resources to study" in command:
        talk("Udemy now active on your device.")
        udemy='https://www.udemy.com/?ranMID=39197&ranEAID=hL6ObH*7r3M&ranSiteID=hL6ObH.7r3M-eGxjarBaizWoJAZTUbCmtQ&LSNPUBID=hL6ObH*7r3M&utm_source=aff-campaign&utm_medium=udemyads'
        webbrowser.open_new_tab(udemy)
    elif 'need to study cybersecurity' in command:
        talk("Preparing Hack the box")
        htb='https://academy.hackthebox.com/modules'
        webbrowser.open_new_tab(htb)
    elif 'display analyzed data' in command:
        talk("Starting Power BI")
        powerbi=''
        webbrowser.open_new_tab(powerbi)
    else:
        talk('Please say the command again.')
#--------------------------------------------------------------------------------------------------------------------------------------

introduction()

while True:
    run_jarvis()
#--------------------------------------------------------------------------------------------------------------------------------------