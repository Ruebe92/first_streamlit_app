import requests
import streamlit
import pandas
import snowflake.connector
from urllib.error import URLError


streamlit.title("MY Mom's New Healthy Diner")
streamlit.text("🥝🍇🍈 Omega 3  Blueberry Oatmeal")
streamlit.text("🍌🍑🍉Kale, Spinach & Rocket Smoothie")
streamlit.text("🍓🍒🥥Hard-Boiled Free-Range Egg")
streamlit.text("🍈🍐🍏Avocado Toast")

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

# Fruitlist from .txt
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado','Strawberries'])
streamlit.dataframe(my_fruit_list)
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)

# Fruitlist from Fruityvice API
streamlit.header("Fruityvice Fruit Advice!")
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)

def get_fruityvice_data(this_fruit_choice):

    fruityvice_response = requests.get(f"https://fruityvice.com/api/fruit/{this_fruit_choice}")
    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())

    return fruityvice_normalized

streamlit.header('Fruityvice Fruit Advice:')
try:
    fruit_choice = streamlit.text_input('What fruit would you like to look up on Fruityvice?')

    if not fruit_choice:
        streamlit.error("Please select a fruit to get information.")
    else:

        fruit = get_fruityvice_data(fruit_choice)
        streamlit.dataframe(fruit)

except URLError as e:
    streamlit.error()

# Fruityvice API Response
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * FROM PC_RIVERY_DB.PUBLIC.FRUIT_LOAD_LIST;")
my_data_rows = my_cur.fetchall()
streamlit.header("The fruit load contains:")
streamlit.dataframe(my_data_rows)

add_my_fruit = streamlit.text_input('What fruit would you like to add?','Jackfruit')

streamlit.write('Thanks for adding ', add_my_fruit)

my_data_rows = my_data_rows.append(add_my_fruit)
my_cur_execute("insert into freuit_load_list values ('from streamlit')")
## Food-API-Key: 1dkQOdxq2n1nH09C3cjzexdiGvzOd0UcGmuWlK0T 

