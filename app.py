import streamlit as st
from PIL import Image

st.title("Mi primera app")

st.header("En este espacio comienzo a desarrollar mis aplicaciones para interfaces")
st.write("Facilmente puedo realizar back-end y front-end")
image = Image.open('Travis meme.png')

st.image(image, caption='interfaces multimodales')



texto = st.text_input('Escrible algo', 'Este es mi texto')
st.write('El texto escrito es', texto)
st.subheader("Ahora usemos 2 columnas")
