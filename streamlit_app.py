import requests
import streamlit
import pandas

streamlit.title("MY Mom's New Healthy Diner")
streamlit.text("🥝🍇🍈 Omega 3  Blueberry Oatmeal")
streamlit.text("🍌🍑🍉Kale, Spinach & Rocket Smoothie")
streamlit.text("🍓🍒🥥Hard-Boiled Free-Range Egg")
streamlit.text("🍈🍐🍏Avocado Toast")

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado','Strawberries'])

streamlit.dataframe(my_fruit_list)

fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)

streamlit.header("Fruityvice Fruit Advice!")
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response.json())


## Food-API-Key: 1dkQOdxq2n1nH09C3cjzexdiGvzOd0UcGmuWlK0T 