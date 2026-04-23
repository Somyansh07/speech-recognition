import speech_recognition as sr
import webbrowser
import pyttsx3
import asyncio
import google.generativeai as genai
import musiclibrary
import requests

recognizer = sr.Recognizer()

newsapi = "pub_a88bd57da96e43148e5375ef7f3d613a"


def songss (word2):
    song= word2.lower().split(' ',1)[1]
    link =musiclibrary.music.get(song)
    webbrowser.open(link)
    


def speak(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(text)
    engine.runAndWait()
    engine.stop()

speak("hellow sir.")
speak("how are you.")
async def main():
    def processcommand(c):
        if c==1:
            webbrowser.open("https://www.youtube.com")   
        elif c==2:
            webbrowser.open("https://www.instagram.com/")
    def aaaii(textss):
        genai.configure(api_key="AIzaSyD6N4t0eNwGy3rNRZMeJZbwFbRPH7oqWvQ")

        model = genai.GenerativeModel(
            model_name="gemini-2.5-flash",
            system_instruction="You are a helpful talking assistant."
        )

        chat = model.start_chat()

        user_input = textss
        response = chat.send_message(user_input)
        print(response)
        print(response.text)
        speak(response.text)

    while True:
        r = sr.Recognizer() 
        
        try:
            with sr.Microphone() as source:
               print("listening.........")   
               audio = r.listen(source,timeout = 2,phrase_time_limit=1)
            word = r.recognize_google(audio)
            print(word)
            if( "madrachod" == word.lower()):
                speak("active maderchod")
               
                while True :

                    try:
                        with sr.Microphone() as source2:
                            print("listening to your request ...")    
                            audio2 = r.listen(source2,timeout =2,phrase_time_limit=7)
                        word2 = r.recognize_google(audio2)
                        print(word2)
                        if("hey" in word2.lower()) or ("hello" in word2.lower()) or ("hay" in word2.lower()):
                            print(word2)
                            aaaii(word2)
                            break
                        elif "youtube"in word2.lower():
                            speak("opening youtube")
                            print(word2)
                            processcommand(1)
                            break
                        elif "instagram"in word2.lower():
                            speak("opening instragram")
                            print(word2)
                            processcommand(2)
                            break
                        elif "play"in word2.lower():
                            print(word2)
                            songss(word2)
                            break
                        elif "news" in word2.lower():

                            r = requests.get(f"https://newsdata.io/api/1/latest?apikey={newsapi}& country=in")
                            data = r.json()
                            # headlines = []
                            for article in data.get("results", []):
                                title = article.get("title")
                                # if title:
                                #     headlines.append(title)
                            print(title)        
                            speak(title)
                            break
                    except Exception as e:
                        print(f"error 2  ;{e}")
                    
                

        except Exception as e:
            print(f"error  ;{e}")    

if __name__ == "__main__":
    asyncio.run(main())