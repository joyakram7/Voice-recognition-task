
import speech_recognition as sr
#task1
"""
reco = sr.Recognizer()
print("Hello! Say 'exit' to end the conversation.")
while True:
 with sr.Microphone() as source:
    print("Adjusting noise level") 
    reco.adjust_for_ambient_noise(source) 
    print("speak now")
    audio = reco.listen(source) 
    print("recpgnizing speech") 
    try:
    
        text = reco.recognize_google(audio)
        text = text.lower()
        print(f"You said: {text}")

        
        if "exit" in text or "quit" in text:
            print("Conversation ended. Goodbye!")
            break
        elif "hello" in text or "hi" in text:
            print("Hello! How are you?")
        elif "how are you" in text:
            print("I'm fine, thank you for asking!")
        elif "name" in text:
            print("My name is your virtual assistant.")
        elif "weather" in text:
            print("The weather today is sunny and nice!")
        elif "age" in text:
            print("I'm a program, I don't have an age like humans.")
        elif "thanks" in text or "thank you" in text:
            print("You're welcome!")
        else:
            print("Sorry, I didn't understand that. Please try again.")

    except sr.UnknownValueError:
        print("Could not understand audio. Please speak clearly.")
    except sr.RequestError:
        print("Service error. Please check your internet connection.")
"""
#task2

print("Program started")
def access_control(command):
    accepted_commands = ["open", "start", "hello", "login"]

    if command.lower() in accepted_commands:
        return "Access Granted"
    else:
        return "Access Denied"
    
reco = sr.Recognizer()
while True:
    with sr.Microphone() as source:
         print("Adjusting noise level...")
         reco.adjust_for_ambient_noise(source)

         print("Speak now:")
         audio = reco.listen(source)

    print("Recognizing speech...")

    try:
        text = reco.recognize_google(audio)
        print(f" what You said is : {text}")

        if text.lower() == "exit":
            print("Conversation ended.")
            break

        result = access_control(text)
        print(result)

    except sr.UnknownValueError:
        print("I could not understand what you said.")
    except sr.RequestError:
         print("Speech recognition service error.")
         