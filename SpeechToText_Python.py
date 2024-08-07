import speech_recognition as sr #we install speech recognition for audio command and also install pyaudio for audio
import os                      # we use os to run command efficientely
import threading               # we use multithreading to run multiple task at a time
from mtranslate import translate # we use mtranslate to translate the text to any language
from colorama import Fore,Style,init # we use colorma to color the text


init(autoreset=True)
def print_loop():
    #while True:
        print(Fore.GREEN+"Listening..",end="",flush=True)
        print(Style.RESET_ALL,end="",flush=True)

def Translate_hindi_to_english(text):
    english_text = translate(text,"en-us")
    return english_text
def Speech_TO_Text_Python():
    recognizer = sr.Recognizer()
    recognizer.dynamic_energy_threshold = False
    recognizer.energy_threshold = 34000
    recognizer.dynamic_energy_adjustment_damping = 0.010
    recognizer.dynamic_energy_ratio = 1.0
    recognizer.pause_threshold = 0.8
    recognizer.operation_timeout = None
    recognizer.pause_threshold = 0.2
    recognizer.non_speaking_duration = 0.2

    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        while True:
            print(Fore.GREEN+"Listening..",end="",flush=True)
            try:
                audio = recognizer.listen(source,timeout=3)
                print("\r" + Fore.RED+"Processing..",end="",flush=True)
                recognizer_text = recognizer.recognize_google(audio).lower()
                if recognizer_text:
                    trans_text = Translate_hindi_to_english(recognizer_text)
                    print("\r" +Fore.BLUE+"You said: ",trans_text)
                    return trans_text
                else:
                    return ""
            except sr.UnknownValueError:
                recognizer_text = ""
            
            finally:
                print("\r" ,end="",flush=True)
            os.system("cls" if os.name == "nt" else "clear")

        stt_thread = threading.Thread(target=print_loop)
        stt_thread.start()
        print_loop.start()
        stt_thread.join()
        print_loop.join()

Speech_TO_Text_Python()
            

