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
    
radio_but=st.sidebar.radio("Your Selection",["Male","Female"])
if radio_but=="Male":
    st.info("You are Male")
else:
    st.info("You are Female")

city=st.sidebar.selectbox("Your City",["Daman","Diu","Valsad"])
if city=="Daman":
    st.info("I love Daman")
elif city=="Diu":
    st.info("I love Diu")
else:
    st.info("I love Valsad")

occupation=st.multiselect("Your Occupation",["Programmer","Data Scientist","ITConsultant","DBA"])

age=st.number_input("Input a Number")

message=st.text_area("About NIELIT","WRITE SOMETHINGS-----")
message=st.text_area("address","WRITE SOMETHINGS-----")

select_val=st.slider("select a value",1,10)
#starting value = 10.0 ending value = 20.0 increment by 0.5
select_val1=st.slider("select a value",10.0,20.0,0.5)
if st.button("Balloons"):
    st.balloons() 
    
#-----pandas dataframe-----#
import streamlit as st
import pandas as pd

auto_data=pd.read_csv("auto.csv")
st.dataframe(auto_data.head())

st.table(auto_data.head(10))

st.area_chart(auto_data[["mpg","cylinders"]])
st.area_chart(auto_data[["mpg","cylinders"]].head(20))

st.bar_chart(auto_data[["mpg","cylinders"]])
st.bar_chart(auto_data[["mpg","cylinders"]].head(20))

st.line_chart(auto_data[["mpg","cylinders"]])
st.line_chart(auto_data[["mpg","cylinders"]].head(20))

import datetime
import time
today=st.date_input("Today is",datetime.datetime.now())
hour=st.time_input("The time is",datetime.time(12,30))

st.code("import pandas as pd")
st.code("print(welcome to NIELIT Daman)")

import pandas as pd
import numpy as np

st.title("Area")
df=pd.DataFrame(np.random.randn(40,4),columns=["C1","C2","C3","C4"])
st.bar_chart(df)

st.title("Line Chart")
df=pd.DataFrame(np.random.randn(40,4),columns=["C1","C2","C3","C4"])
st.line_chart(df)

st.title("Area Chart")
df=pd.DataFrame(np.random.randn(40,4),columns=["C1","C2","C3","C4"])
st.area_chart(df)