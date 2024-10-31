import speech_recognition as sr
import pyttsx3
import pywhatkit as pyw
import datetime
import wikipedia

# Initialize the recognizer and text-to-speech engine
listener = sr.Recognizer()
machine = pyttsx3.init()

def talk(text):
    machine.say(text)
    machine.runAndWait()

def input_instruction():
    global instruction
    try:
        with sr.Microphone() as source:
            print("Listening...")
            speech = listener.listen(source)
            instruction = listener.recognize_google(speech)  # Fixed method name
            instruction = instruction.lower()
            if "alex" in instruction:
                instruction = instruction.replace('alex', "").strip()  # Fixed typo and added strip()
                print(instruction)
    except sr.UnknownValueError:
        talk("Sorry, I did not understand that.")
        return ""
    except sr.RequestError:
        talk("Sorry, there was an issue with the speech recognition service.")
        return ""
    return instruction

def play_p():
    instruction = input_instruction()
    print(instruction)
    if "play" in instruction:
        song = instruction.replace('play', "").strip()  # Fixed typo
        talk("Playing " + song)
        pyw.playonyt(song)
    
    elif 'time' in instruction:
        current_time = datetime.datetime.now().strftime('%I:%M %p')  # Fixed method name
        talk('Current time is ' + current_time)

    elif 'date' in instruction:  # Fixed 'data' to 'date' for clarity
        date = datetime.datetime.now().strftime('%d/%m/%Y')
        talk("Today's date is " + date)
        
    elif 'how are you' in instruction:
        talk('I am fine, how about you?')

    elif 'what is your name' in instruction:  # Fixed 'What is your name' to match lower-case comparison
        talk('I am Alex. What can I do for you?')

    elif 'who is' in instruction:
        human = instruction.replace('who is', "").strip()
        try:
            info = wikipedia.summary(human, 1)
            pri
            talk(info)
        except wikipedia.exceptions.DisambiguationError as e:
            talk("There are multiple results, please be more specific.")
        except wikipedia.exceptions.PageError:
            talk("I couldn't find any information on that topic.")
        
    else:
        talk('Please repeat.')

# Run the function to test
play_p()