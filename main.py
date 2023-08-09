import pyttsx3
from api_key import openai_key
import Al
import gtts as gt
import streamlit as st
from streamlit_modal import Modal
import speech_recognition as sr
import base64
import pyaudio
LANGUAGE_CODES = {
    "English": "en",
    "German": "de",
    "Hindi": "hi",
    "Chinese": "zh",
    "French": "fr",
    "Spanish": "es",
    "Japanese": "ja",
    "Korean": "ko",
    "Arabic": "ar"
}
def main():
    st.title("Text To Audio")
    input_text = st.text_area("Please Enter your Text here: ")
    language1 = st.selectbox("Select Language", list(LANGUAGE_CODES.keys()))
    if st.button("Submit  "):
        engine = pyttsx3.init()
        if(len(input_text) == 0):
            engine.setProperty('rate',110)
          # engine.say("Chutiiiyyye Kuch likh toh sahhiii behen ke loddde")
            st.warning("LIKH LE MERE BHAI")
            engine.runAndWait()
        else:
            engine.setProperty('voice',language1)
            engine.setProperty('rate',130)
            engine.say(input_text)
            engine.runAndWait()
    if st.button("Download"):
        tts = gt.gTTS(text=input_text, lang=LANGUAGE_CODES[language1])
        audio_filename = "audio_file.mp3"
        tts.save(audio_filename)

        with open(audio_filename, "rb") as audio_file:
            audio_contents = audio_file.read()
            b64_audio = base64.b64encode(audio_contents).decode()

        href = f'<a href="data:audio/mp3;base64,{b64_audio}" download="{audio_filename}">Click here to download</a>'
        st.markdown(href, unsafe_allow_html=True)
#################################################################################################################
    st.title("Langauage Changer")
    input_text2 = st.text_area("Enter The Text You Want translate")
    language02 = st.selectbox("Select Your Language", list(LANGUAGE_CODES.keys()))
    language03 = st.selectbox("Select To Language",list(LANGUAGE_CODES.keys())) 
    if st.button("Translate"):
        if(len(input_text2)== 0):
            st.warning("Please Write Text You Want to Translate!!!")
        else:
            st.write(Al.text_translation(input_text2,language02,language03))
#######################################################################################################################3
    st.title("Voice to Text")
    
    speaks = st.button("Speak")
    if(speaks):
            st.write("Please Say something!")
            recognizer = sr.Recognizer()
            mic = sr.Microphone()
            try:
                with mic as source:
                    audio = recognizer.listen(source,timeout=20)
                text = recognizer.recognize_google(audio)
                st.write("You Said:",text)
                engine2 = pyttsx3.init()
                engine2.setProperty('voice','english')
                engine2.setProperty('rate',130)
                engine2.say(text)
                engine2.runAndWait()
                '''if(text == 'how are you' or "How are you"):
                    engine2.setProperty('voice','english')
                    engine2.setProperty('rate',130)
                    engine2.say('I am fine what about you')
                    engine2.runAndWait()'''
            except sr.UnknownValueError:
                st.write("Sorry Your Voice is Not understandable")
            except sr.RequestError as e:
                st.write("Could not request results; {0}".format(e))
if __name__=="__main__":
    main()