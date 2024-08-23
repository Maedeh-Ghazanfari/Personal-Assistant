import pyttsx3
import time
import speech_recognition as sr

# Speech recognition
r = sr.Recognizer()
source = sr.Microphone()
wake_up = [('Hello', 1), ('Hey MA', 1)]


def speak(text):
    rate = 100
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', rate + 50)
    engine.say(text)
    engine.runAndWait()


def start():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
    # data = ""
    try:
        data = r.recognize_google(audio)
        data.lower()
        print("You said: " + data)
        if "how are you" in data:
            speak("I am Fine")
        elif "hello" in data:
            speak("Hi there")
        else:
            speak("I'm sorry, I did not understand your request")
    except sr.UnknownValueError:
        speak('Sorry, did not understand your request!')

    except sr.RequestError as e:  # if you get a request error from Google speech engine
        print("Could not request results from Google Speech Recognition service; {0}".format(e))


def call(recognizer, audio):
    try:
        my_speech = recognizer.recognize_sphinx(audio, keyword_entries=wake_up)
        if 'MA' or 'Hey MA' in my_speech:
            speak('Yeap?')
    except sr.UnknownValueError:
        speak('Sorry, I could not catch that!')


def listen():
    r.listen_in_background(source, wake_up)
    time.sleep(10000)


speak('Hello Maedeh')

while True:
    start()
