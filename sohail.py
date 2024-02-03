import speech_recognition as sr
import googletrans
import pyttsx3

def convert_speech_to_text_and_translate():
    # Initialize the recognizer
    recognizer = sr.Recognizer()
    
    # Use the default microphone as the audio source
    with sr.Microphone() as source:
        print("Say something...")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
        audio = recognizer.listen(source, timeout=10)  # Listen to the audio for a maximum of 10 seconds
        
        try:
            # Use the Google Web Speech API to recognize the speech
            text = recognizer.recognize_google(audio)
            print("You said:", text)
            
            # Translate the recognized text to a different language using Google Translate API
            translated_text = translate_text(text, target_language='fr')  # Change 'fr' to the desired language code
            print("Translated text:", translated_text)
            
            # Speak out the translated text
            speak_text(translated_text)
        
        except sr.UnknownValueError:
            print("Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print(f"Could not request results from Google Web Speech API; {e}")

def translate_text(text, target_language='fr'):
    # Initialize the Translator
    translator = googletrans.Translator()
    
    # Translate the text to the target language
    translation = translator.translate(text, dest=target_language)
    translated_text = translation.text
    return translated_text

def speak_text(text):
    # Initialize the text-to-speech engine
    engine = pyttsx3.init()
    
    # Set properties for speech
    engine.setProperty('rate', 150)  # Speed of speech
    engine.setProperty('volume', 1)   # Volume level
    
    # Speak out the text
    engine.say(text)
    
    # Wait for speech to finish
    engine.runAndWait()

if __name__ == "__main__":
    convert_speech_to_text_and_translate()