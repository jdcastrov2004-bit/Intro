import streamlit as st
from PIL import Image

st.title("Mi primera app")

st.header("En este espacio comienzo a desarrollar mis aplicaciones para interfaces")
st.write("Facilmente puedo realizar back-end y front-end")
image = Image.open('Travis meme.png')

st.image(image, caption='interfaces multimodales')

