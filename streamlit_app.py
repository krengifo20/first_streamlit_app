import streamlit
import pandas as pd
streamlit.title('Hi, greetings from VSCode')
streamlit.header('Welcome to Streamlit')
streamlit.text('Shall we have a drink?')
streamlit.text('Or shall we have some food?')
streamlit.text('Choose one: 🥣 🥗 🐔 🥑🍞')
streamlit.header('Get some breakfast better:')
streamlit.text('🥣Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞Avocado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pd.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')

# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

streamlit.dataframe(my_fruit_list)
