# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import streamlit as st
import plotly.express as px
import pandas as pd
import plotly.figure_factory as ff

import pickle
with st.sidebar:
    st.write("Este es una barra lateral")

import streamlit as st

option = st.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone'))
df = px.data.gapminder()
st.dataframe(df)
listaPaises = df["country"].unique()
st.write(listaPaises)
pais = "Canada"
with st.sidebar:
    pais = st.selectbox("Paises", listaPaises)
    st.write(pais)
datoPais = df.query("country == ' " + pais + "'")
fig = px.bar(datoPais, x='year', y='pop')
st.plotly_chart(fig, use_container_width=True)

valor = st.slider('Elige el rango de años a anlizar', 1950, 2010, 1990)
st.write("Elegiste", valor)

datosFiltrados= datoPais[datoPais["year"] == valor]
st.dataframe(datosFiltrados)


    # Use a breakpoint in the code line below to debug your script.
    st.header("Hola desde streamlit!")
    st.subheader("Probando..1..2..3")
    st.write("Hola, soy ximena")
    st.write("Esta es la clase de Herramientas3")
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Hi Ximena')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
