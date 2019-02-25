import speech_recognition as sr
import pyaudio


r = sr.Recognizer()
val = 'y'

while val == 'y':
    with sr.Microphone() as source:
        print("Speak Anything :")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio,language = 'es-ES')
            print("You said : {}".format(text))
        except:
            print("Sorry could not recognize what you said")
        
        val = input('Desea volver a intentar y/n : ')