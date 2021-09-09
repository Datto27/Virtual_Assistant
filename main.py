# its working properly but need some updates, add commands
import speech_recognition as sr
import pyttsx3
import pywhatkit  # for playing youtube music
import datetime
import wikipedia

listener = sr.Recognizer()
engine = pyttsx3.init()

# # for women voice
# voices = engine.getProperty("voices")
# engine.setProperty("voice", voices[1].id)


def talk(txt):
    engine.say(txt)
    engine.runAndWait()


def rec_audio():
    try:
        print("listenting...")
        with sr.Microphone() as source:
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            # if "alexa" in command:
            # print(command)
            # talk(command)
    except:
        pass

    return command


def main_run():
    command = rec_audio()
    print(f"==>{command}")
    if "hello" in command:
        talk("hi")
    elif "play" in command:
        song = command.replace("play", "")
        talk("playing " + song)
        print(song)
        pywhatkit.playonyt(song)
    elif "time" in command:
        time = datetime.datetime.now().strftime("%H:%M")
        print(time)
        talk("current time is "+time)
    elif "info" in command:
        person = command.replace("info", "")
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif "are you single" in command:
        talk("I am in a relationship with wifi")
    elif "exit" in command:
        exit()
    else:
        talk("Please say that again")


while True:
    main_run()
