import streamlit
import pandas as pd
import requests
import snowflake.connector
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
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruit_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado', 'Strawberries'])
fruit_to_show = my_fruit_list.loc[fruit_selected]

streamlit.dataframe(fruit_to_show)


streamlit.header("Fruityvice Fruit Advice!")

# streamlit.text(fruityvice_response.json())

fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
if fruit_choice != '':
    streamlit.write('The user entered ', fruit_choice)

    fruityvice_response = requests.get(f'https://fruityvice.com/api/fruit/{fruit_choice}')
    # write your own comment -what does the next line do? 
    fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
    # write your own comment - what does this do?
    streamlit.dataframe(fruityvice_normalized)
else:
    streamlit.write('Please, enter a fruit name')

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * pc_rivery_db.public.fruit_load_list")
my_data_row = my_cur.fetchall()
streamlit.header("The fruit list contains: ")
streamlit.text(my_data_row)