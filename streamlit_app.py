import requests
import streamlit
import pandas

streamlit.title("MY Mom's New Healthy Diner")
streamlit.text("π₯ππ Omega 3  Blueberry Oatmeal")
streamlit.text("πππKale, Spinach & Rocket Smoothie")
streamlit.text("πππ₯₯Hard-Boiled Free-Range Egg")
streamlit.text("πππAvocado Toast")

streamlit.header('ππ₯­ Build Your Own Fruit Smoothie π₯π')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado','Strawberries'])

streamlit.dataframe(my_fruit_list)

fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)

streamlit.header("Fruityvice Fruit Advice!")
fruit = "banana"
fruityvice_response = requests.get(f"https://fruityvice.com/api/fruit/{fruit}")

#Normalize json with pandas
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
streamlit.dataframe(fruityvice_normalized)

fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)

## Food-API-Key: 1dkQOdxq2n1nH09C3cjzexdiGvzOd0UcGmuWlK0T 