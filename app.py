import streamlit as st
from PIL import Image

st.title("🔥 Mi primera app interactiva 🔥")

st.header("Aquí empieza mi aventura con las interfaces multimodales 😎")

st.write(
    "En este espacio empiezo a crear mis propias apps, mezclando diseño y un poco de flow. "
    "Aquí puedo conectar el **back-end** con el **front-end** (Todavía no se muy bien que son) sin complicarme demasiado."
)

image = Image.open('Travis meme.png')
st.image(image, caption='Un toque de humor para las interfaces 😄')

texto = st.text_input('💬 Escribe algo aquí:', '¡Hola mundo! jajajaja')
st.write('🪄 Tu texto dice:', texto)
st.subheader("✨ Ahora juguemos con dos columnas")
