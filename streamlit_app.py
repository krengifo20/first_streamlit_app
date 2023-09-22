import streamlit
import pandas as pd
import requests
import snowflake.connector
from urllib.error import URLError


def get_fruityvice_data(fruit):
    fruityvice_response = requests.get(f'https://fruityvice.com/api/fruit/{fruit_choice}') 
    fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
    return fruityvice_normalized

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

try:
    fruit_choice = streamlit.text_input('What fruit would you like information about?')
    if fruit_choice != '':
        # streamlit.write('The user entered ', fruit_choice)

        fruityvice_normalized = get_fruityvice_data(fruit_choice)
        streamlit.dataframe(fruityvice_normalized)
    else:
        streamlit.error('Please, enter a fruit name')
except URLError as e:
    streamlit.error()


def get_fruit_list():
    with my_cnx.cursor() as my_cur:
        my_cur.execute("SELECT * FROM pc_rivery_db.public.fruit_load_list")
        return my_cur.fetchall()



streamlit.header('Show fruit list')
if streamlit.button('Show fruit list'):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    my_data_row = get_fruit_list()
    streamlit.dataframe(my_data_row)


def insert_row_fruit(new_fruit):
    with my_cnx.cursor() as my_cur:
        my_cur.execute("insert into pc_rivery_db.public.fruit_load_list values ('from streamlit')")
        return 'Thanks for adding' + new_fruit

add_fruit = streamlit.text_input('Do you want to add some fruit?')
if add_fruit != '':
    if streamlit.button('Add fruit'):
        my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
        text_back = insert_row_fruit(add_fruit)
        streamlit.text(text_back)

streamlit.stop()
