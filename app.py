import streamlit as st
from PIL import Image

st.title("Efecto Punch")

st.header("Tal vez no amamos a Punch solo por tendencia, sino porque conecta con esas versiones nuestras que alguna vez se sintieron igual.")
st.write("Este espacio no es solo fandom. Es una pequeña exploración sobre empatía, identificación y esos momentos en los que también fuimos un poco Punch.")
image = Image.open('img.png')

st.image(image, caption='Interfaces multimodales')


texto = st.text_input('Escribe algo', 'Este es mi texto')
st.write('El texto escrito es', texto)

st.subheader("Ahora usemos 2 Columnas")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Esta es la primera columna")
    st.write("Las interfaces multimodales mejoran la experiencia de usuario")
    resp = st.checkbox('Estoy de acuerdo')
    if resp:
       st.write('Correcto!')

