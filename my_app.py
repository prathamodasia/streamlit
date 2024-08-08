import streamlit as st

st.write("Hello World: Getting Bore, Hello Brother!!")
st.title("Display title use st.title()")
st.write("To write text use st.write()")
st.header("I am header to write header use st.header()")
st.subheader("I am subheader to write header use st.subheader()")
st.text("Hey I am simple text to write simple text use st.text()")
st.markdown("[Streamlit](https://streamlit.io/)")
st.markdown("[Streamlit CheatSheet](https://cheat-sheet.streamlit.app/)")
st.success("Success!")
st.info("Information")
st.warning("This is a warning")
st.error("This is an error!")

from PIL import Image
img=Image.open("smj.jpg")
st.image(img, width=300, caption="Satyamev Jayate")

video_file=open("vid.mp4","rb")
video_bytes=video_file.read()
st.video(video_bytes)

st.video("https://www.youtube.com/watch?v=2v8urSwf8TI")

audio_file=open("song.mp3","rb")
audio_bytes=audio_file.read()
st.audio(audio_bytes,format="audio/mp3")

st.button("Play")
st.header("Button Widgets")

if st.button("Play1"):
    st.text("Hello World")

if st.button("Play2"):
    st.text("Enjoy Music")
    st.video("https://www.youtube.com/watch?v=2v8urSwf8TI")
    
if st.checkbox("Checkbox"):
    st.text("Checkbox selected")
    st.video("https://www.youtube.com/watch?v=pGG_Zosn-qo&list=PLsm6x0zLuEYKUyUSORRbETUlzJZrIwvrS")