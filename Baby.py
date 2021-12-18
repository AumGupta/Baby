"""
BABY - The Assistant
    - This is a very basic assistant sofware 
    made mojorly with pygame that recognizes users voice commands only in
    english language on keyword and some direct statement basis and
    gives relevant information is possible.
    -It's name is a pun.

What it can do?
    - Search for anything on the internet.
    - Ask her to open any website on webbrowser.
    - Ask her to play any song by the keyword "play".
    - Find discriptions of various personalities by the keyword "who is".
    - Tell the time.
    - Tell the Date.
    - Tell the Day of Week.
    - User can tell her that its their birthday and see the magic.
    - Ask her to tell a joke.
    - Many more interesting tasks.

Project Details:
    Started on - 19 Dec, 2020
    Created By - Om Gupta
    Supported OS - Microsoft Windows
    Modules Used:
        - Standard Library Modules:
            -sys
            -os
            -time
            -datetime
            -random
            -webbrowser
        - Additional Modules:
            - pygame
            - speech_recognition
            - pyttsx3
            - pywhatkit
            - wikipedia
            - googlesearch
            - joke
            - pyjokes
"""

# Importing Required Standard Lib Modules
from math import fabs
import random, sys, os, datetime, webbrowser
import time as t

# Safe importing the Additional Modules
def downloadModule(module = "") -> str: #Give module name as in documentation in strings
    """
    Installs the module through command line using pip.
    """
    os.system('cls')
    try:
        os.system('cmd /c "pip -v"')
        os.system('cls')
    except:
        print('\n\t`pip` COMMAND NOT FOUND WHICH IS NEEDED FOR DOWNLOADING MODULE! \n')
        try:
            os.system('cmd /c "curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py"')
        except:
            print('\n\n\t KINDLY INSTALL PIP MANUALLY!\n\n\n')
            
        os.system('cmd /c "python get-pip.py"')
    
    print('\n\tDOWNLOADING MISSING MODULE : '+module+' :\n')
    os.system('cmd /c "pip install ' + module)
    os.system('cls')

try:
    import pygame as p
    os.system('cls')
except:
    downloadModule("pygame")
    import pygame as p
    os.system('cls')


try:
    import speech_recognition
except:
    downloadModule("SpeechRecognition")
    import speech_recognition

try:
    import pyaudio #For using Microphone as source
except:
    downloadModule("pipwin")
    os.system('cmd /c "py -m pipwin install pyaudio')
    os.system('cls')

try:
    import pyttsx3 #For converting text to speech
except:
    downloadModule("pypiwin32")
    downloadModule("wheel")
    downloadModule("-U setuptools")
    downloadModule("pyttsx3==2.90")
    import pyttsx3

try:
    import pywhatkit
except:
    downloadModule("pywhatkit")
    import pywhatkit

try:
    import wikipedia
except:
    downloadModule("wikipedia")
    import wikipedia

try:
    import googlesearch
except:
    downloadModule("beautifulsoup4")
    downloadModule("google --user")
    import googlesearch

try:
    import pyjokes as pj
except:
    downloadModule("pyjokes")
    import pyjokes as pj

try:
    from joke.jokes import icanhazdad
except:
    downloadModule("axju-jokes")
    from joke.jokes import icanhazdad


 
# Required only while Packaging
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

resource_path('Fonts\Font.ttf')
resource_path('Sounds\click.mp3')
resource_path('Sounds\listen.mp3')
resource_path('Images\Background.png')
resource_path('Images\micdown.png')
resource_path('Images\iconSmall.png')
resource_path('Images\listen.png')
resource_path('Images\hoverbutton.png')

def about(introMsg = "Hi i am baby, I am the creation of Mr.Om Gupta. What I can do? Search for anything on the internet, open any website, play any song, find any personalities' summary, tell the time, Date and Day of Week, wish you HAPPY BIRTHDAY, make you laugh with a joke and many more interesting stuff! ------To close me you can say bye bye or go or any such line")-> str:
    """
    Small discription of the project which is spoken when called.
    """
    p.mouse.set_cursor(p.SYSTEM_CURSOR_WAITARROW)

    blitPara(introMsg, wordsPerLine=7, lineSpacing=120)
    speakText(introMsg.replace("Om Gupta","Owm Goopta"))
    # speakText("Hi i am baby, I am the creation of Mr.Owm Goopta.")

def intro():
    """
    For introduction
    """
    blitBig("Hi!", 200, 200)
    speakText("Hi!")
    p.display.update(screen.fill("black"))

    blitBig("I'm", 200, 180)
    blitBig("Baby",170,290)
    speakText("I'm Baby")
    p.display.update(screen.fill("black"))

    blitBig("I'd love to help",x=30,y=200)
    blitBig("you!",180,310)
    speakText("I'd love to help you")
    p.display.update(screen.fill("black"))
    

def blit(text, x=100, y=100):
    """
    Display `text` on screen.

    Keyword arguments:

    * x - x-coordinate of text
    * y - y-coordinate of text
    """
    txt = smallFont.render(text, True, (30, 30, 30))
    p.display.update(screen.blit(txt, (x, y)))

def blitBig(text, x=100, y=100):
    """
    Display `text` on screen.

    Keyword arguments:

    * x - x-coordinate of text
    * y - y-coordinate of text
    """
    txt = bigFont.render(text, True, (255, 255, 255))
    p.display.update(screen.blit(txt, (x, y)))

def blitPara(text, wordsPerLine = 5, lineSpacing = 100):
    """
    Display paragraph `text` on screen.

    Keyword arguments:

    * wordsPerLine - (number) Number of words to be written in a single line
    * lineSpacing - (number) Space between two lines
    """
    x = text.split()
    a = 0
    b = wordsPerLine
    for i in range(len(x)):
        n = x[a:b]
        r = ''
        for j in n:
            r += j + ' '
        p.display.update(blit(r, 60, lineSpacing))
        a += wordsPerLine
        b += wordsPerLine
        lineSpacing += 20

def cleanText(text, erase):
    """
    Erases a part of the `text`.
    
    Arguments:

    * text - (string) a string which has to be cleaned
    * erase - (string) Part of text to be erased
    """
    new_text = text.replace(erase, '')
    return new_text

def speakText(text):
    """
    Converts string in `text` to speech.
    """
    engine.say(text)
    engine.runAndWait()

def playSound(filename) ->str:
    """
    Plays the audio file at `filename`
    """
    p.mixer.music.load(filename)
    p.mixer.music.play()



def listen():
    """
    Prepares microphone for listening to a command and 
    returns the command if command started with `baby`
    """
    try:
        with speech_recognition.Microphone() as source:

            p.mouse.set_cursor(p.SYSTEM_CURSOR_WAITARROW)
            listener.adjust_for_ambient_noise(source)
            p.mouse.set_cursor(p.SYSTEM_CURSOR_ARROW)
            
            p.display.update(screen.blit(listening, (0, 0)))
            blit("Listening...")

            playSound("Sounds\listen.mp3")

            voice = listener.listen(source, timeout=5)
            command = listener.recognize_google(voice)
            command = command.lower()
            print("\nCommand:\n",command,"\n")
            if 'baby' in command:
                command = cleanText(command, 'baby')
                return command
            else:
                speakText("Please call my name baby, and then give the command")
    except:
        speakText("Your words are not clear or your mike isn't connected")
        speakText("please try again")

def googleit(text) -> str:
    """
    Search the given query string using Google and opens it in the default browser
    """
    try:
        url = googlesearch.search(text, tld='com', lang='en', num=1, stop=1, pause=2.0)
        for i in url:
            print(i)
            webbrowser.open(i)
    except :
        webbrowser.open("https://www.google.com/search?q="+text)

def actionBaby():
    """
    Initiate fetching and analyzation of command from user.
    """
    try:
        runState = True

        # Setting mic button up 
        t.sleep(.1)
        p.display.update(screen.blit(background, (0, 0)))
        p.display.update(screen.blit(credits,(385,570)))
        p.display.update(screen.blit(aboutIcon, (485, 5)))

        # Fetch the command from user 
        os.system("cls")       
        command = listen()

        # Resetting the screen
        p.display.update(screen.blit(background, (0, 0)))
        p.display.update(screen.blit(credits,(385,570)))
        p.display.update(screen.blit(aboutIcon, (485, 5)))

        
        # ANALYSING THE COMMAND

        # Command types for direct interaction
        disrespectfulStatements = [
            'are you mad',
            'are you crazy',
            'have you gone nuts',
            'get lost']
        
        healthQuestions = [
            "how are you",
            "what's up",
            "what you doing",
            "are you okay"]

        userAffectionQuestions = [
                "do you like me",
                "do you love me",
                "what do you think about me"
            ]
        
        exitStatements = [
            "you can leave",
            "close yourself",
            "you may leave",
            "you can go now",
            "exit yourself",
            "bye bye",
            "you can go"
            ]
        
        # Keyword based analysis of command
        if 'play' in command:
            song = command.replace('play', '')
            p.display.update(blitPara('Playing' + song + ' for you...'))
            speakText('Playing' + song + ' for you')
            pywhatkit.playonyt(song)

        elif 'search' in command:
            command = command.replace("search ", "")
            p.mouse.set_cursor(p.SYSTEM_CURSOR_WAITARROW)
            
            p.display.update(blit("Please wait..."))
            p.display.update(blitPara('Searching ' + command + '...'))
            
            speakText("Please wait")
            speakText('Searching ' + command)
            
            if 'search for' in command:
                command = cleanText(command, 'search for')
                googleit(command)
            elif 'search google for' in command:
                command = cleanText(command, 'search google for')
                googleit(command)
            elif 'search google for what is' in command:
                command = cleanText(command, 'search google for what is')
                googleit(command)
            elif 'search the internet for' in command:
                command = cleanText(command, 'search the internet for')
                googleit(command)
            elif 'search the web for' in command:
                command = cleanText(command, 'search the web for')
                googleit(command)
            else:
                googleit(command)

        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')  # 01 : 01 AM
            p.display.update(blit('It is ' + time))
            time = time.replace(":", " ")
            if 'AM' in time:
                time = time.replace('AM', 'A M')
            if 'PM' in time:
                time = time.replace('PM', 'P M')
            if '0' in time[0] or '0' in time[3]:
                time = time.replace('0', ' ')
            speakText('it is' + time)

        elif "date" in command:
            date = datetime.datetime.now().date()
            p.display.update(blit("Today is " + str(date)))
            speakText("Today is " + str(date))

        elif "your name" in command:
            p.display.update(blit("My name is baby ... just baby"))
            speakText('My name is baby, just baby.')

        elif "birthday" in command:
            p.display.update(blit("Happy Birthday to you"))
            speakText("Happy Birth day to you")
            speakText("here is a song for you ")
            songListHBD = [
                "Best Happy Birthday To You | Happy Birthday Songs Remix 2020",

                "Birthday Song ❤️ Best Good Wishes For Your Birthday 2021 WhatsApp Happy Bday Lyrics Video for adults",

                "Aww Tera Happy Bday|ABCD 2 |Varun Dhawan Shraddha Kapoor |Sachin - Jigar |D.Soldierz | Birthday song"
            ]
            selectedSongHBD = random.choice(songListHBD)
            pywhatkit.playonyt(selectedSongHBD)
            speakText('in joy.')

        elif 'day' in command:
            day_name = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
            day = datetime.datetime.weekday(datetime.datetime.today())
            p.display.update(blit("Today is " + day_name[day]))
            speakText("today is " + day_name[day])

        elif 'who created you' in command :
            blit('Om Gupta created me')
            speakText('owm goopta created me.')

        elif 'who is ' in command:
            print(command)
            try:
                person = command.replace('who is ', '')
                print(person)
                if 'om gupta' in command:
                    blit('Om Gupta is my creator.')
                    speakText('Owm Goopta is my creator')
                else:
                    blit(person.upper(),50,50)
                    info = wikipedia.summary(person, sentences = 2)
                    print(info)

                    blitPara(info)

                    s = info.split(".")
                    for j in s:
                        speakText(j)
            except:
                p.display.update(blit("This is what I found on internet..."))
                p.mouse.set_cursor(p.SYSTEM_CURSOR_WAITARROW)
                speakText("This is what I found on internet")
                cleanText(command, 'who is ')
                googleit(command)

        elif "website of" in command:
            try:
                search = command.replace("open", "")
            except:
                pass

            p.display.update(blit("Please wait... Opening", x=60,y=80))
            
            blitPara(search)

            p.mouse.set_cursor(p.SYSTEM_CURSOR_WAITARROW)

            speakText("Please wait")
            speakText("Opening" + search)
            googleit(search)

        elif "joke" in command:
            joke_received = random.choice([pj.get_joke('en','neutral'),icanhazdad()])
            blitPara(joke_received,6)
            speakText(joke_received)
            t.sleep(2)
        
        # Direct Interactions - at last because requires more checking
        elif [i for i in disrespectfulStatements if i in command] :
            blit('Sorry! Have I done anything wrong?')
            speakText('Sorry! Have I done anything wrong?')
        
        elif [i for i in healthQuestions if i in command]:
            blitPara("I'm absolutely fine and really happy to see you.", wordsPerLine=7)
            speakText("I'm absolutely fine ,and really happy to see you.")
        
        elif [i for i in userAffectionQuestions if i in command]:
            blitPara("Yeah boss I really like you.", wordsPerLine= 7)
            speakText("Yeahh BOSS! I reeally like you.")
        
        elif [i for i in exitStatements if i in command]:
            blitPara("Ok boss! see you soon")
            speakText("Ok boss! see you soon")
            runState = False
        
        elif not command:
            """
            This will be triggered if only `baby` was spoken 
            and no instruction was passed
            """
            p.display.update(blit("Sorry, I didn't get it. Please try again"))
            speakText("Sorry, I didn't get it. Please try again")

        else:
            command = cleanText(command, command.split()[0]+" ")
            
            p.display.update(blit("Please wait..."))
            p.display.update(blit("Checking for " + command+ " on the internet", 70, 130))
            speakText("Please wait")
            speakText("Checking for " + command + " on the internet")
            webbrowser.open("https://www.google.com/search?q="+command)

        return runState
    except:

        return runState

# Main
if __name__ == "__main__":
    
    # Initiating SpeechRecognition engine
    listener = speech_recognition.Recognizer()
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id) # For changing voice to Female
    engine.setProperty('rate', 170) # for changing rate of speech

    # Initiating pyGame
    p.init()
    clock = p.time.Clock()
    p.display.set_caption("Baby - The Assistant")
    icon = p.image.load("Images\iconSmall.png")
    p.display.set_icon(icon)

    # Setting Up Window
    resolution = (500, 600)
    screen = p.display.set_mode(resolution)
    w = screen.get_width()
    h = screen.get_height()

    # Loading Images
    background = p.image.load('Images\Background.png')
    micDown = p.image.load('Images\micdown.png')
    micHover = p.image.load('Images\hoverbutton.png')
    listening = p.image.load('Images\listen.png')

    # Fonts
    font = p.font.Font("Fonts\Montserrat-Bold.ttf", 20)
    smallFont = p.font.Font("Fonts\Montserrat-Bold.ttf", 15)
    bigFont = p.font.Font("Fonts\Montserrat-Bold.ttf", 56)

    aboutIcon = font.render("?", True, (100, 0, 0))
    aboutIconHover = font.render("?", True, (200, 0, 0))
    credits = smallFont.render("by Om Gupta", True, (90, 90, 90))

    #Click region radius
    radius = 50

    ##Main
    action = True #For running main while loop
    firstLoop = True #to check for first iteration of loop

    while action:
        # Itroductory part for first loop
        if firstLoop:
            intro()
            firstLoop = False
        
        # Setting up the background
        screen.blit(background, (0, 0))
        screen.blit(credits,(385,570))
        screen.blit(aboutIcon, (485, 5))
        
        
        # Getting mouse position 
        mouse = p.mouse.get_pos()

        if w // 2 - radius <= mouse[0] <= w // 2 + radius and h - 100 - radius <= mouse[1] <= h - 100 + radius:
            """
            Triggered while hovering on mic button
            """
            p.mouse.set_cursor(p.SYSTEM_CURSOR_HAND)
            screen.blit(micHover, (0, 0))

        elif 465 <= mouse[0] <= 500 and 0 <= mouse[1] <= 30:
            """
            Triggered while hovering on About button
            """
            p.mouse.set_cursor(p.SYSTEM_CURSOR_HAND)
            screen.blit(aboutIconHover, (485, 5))

        elif 385 <= mouse[0] <= 500 and 570 <= mouse[1] <= 590:
            """
            Triggered while hovering on `by Om Gupta`
            """
            p.mouse.set_cursor(p.SYSTEM_CURSOR_HAND)

        else:
            p.mouse.set_cursor(p.SYSTEM_CURSOR_ARROW)
        
        for event in p.event.get():
            if event.type == p.QUIT:
                engine.stop()
                action = False
            if event.type == p.MOUSEBUTTONDOWN:
                if w // 2 - radius <= mouse[0] <= w // 2 + radius and h - 100 - radius <= mouse[1] <= h - 100 + radius:
                    """
                    Triggered when Mic button is clicked
                    """
                    playSound("Sounds\click.mp3")
                    p.display.update(screen.blit(micDown, (0, 0)))

                    action = actionBaby()

                elif 465 <= mouse[0] <= 500 and 0 <= mouse[1] <= 30:
                    """
                    Triggered when About button is clicked
                    """
                    about()
                elif 385 <= mouse[0] <= 500 and 570 <= mouse[1] <= 590:
                    webbrowser.open("https://www.instagram.com/aaumgupta/")

        p.display.flip()


    # Closing pyGame
    p.quit()
    # Closing the Window
    sys.exit()
