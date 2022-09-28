
import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.title('My Parents New Healthy Diner')

streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

#import pandas

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page.
streamlit.dataframe(fruits_to_show)

#Badge 2  - chapter 9 - REQUESTS 
#New Section to display fruityvice api response
streamlit.header("Fruityvice Fruit Advice!")


#create the repeatable code block (called a function)
def get_fruityvice_data(this_fruit_choice):
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+this_fruit_choice)  
    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
    return fruityvice_normalized



try:
#import requests
#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+"kiwi")
#streamlit.text(fruityvice_response.json()) # Just writes the data to the screen

# take the json version of the response and normalize it 
#fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
#streamlit.text(fruityvice_normalized)
# output it to the screen as a table
#streamlit.dataframe(fruityvice_normalized)

#Variables in Streamlit testing
#Add a Text Entry Box and Send the Input to Fruityvice as Part of the API Call
#fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
     streamlit.error("Please select a fruit to get information")
  else:
     back_from_function = get_fruityvice_data(fruit_choice)
     #streamlit.write('The user entered ', fruit_choice)
     #fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)

     # take the json version of the response and normalize it 
        #fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
     # output it to the screen as a table
     streamlit.dataframe(back_from_function)
except URLError as e:
  streamlit.error() 
#Snowflake.connector code..
#import snowflake.connector. Some reason import snowflake.connector is not working here, so I need to keep at the top of the code

streamlit.stop()

streamlit.header("The fruit load list contains:")
#Snow Flake related functions
def get_fruit_load_list():
    with my_cnx.cursor() as my_cur:
         my_cur.execute("SELECT * from fruit_load_list")
         return my_cur.fetchall()
    
#Add button to load the fruit

if streamlit.button('Get Fruit Load List')
   mycnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
   my_data_rows = get_fruit_load_list()
   streamlit.dataframe(my_data_rows)

#my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
#my_cur = my_cnx.cursor()
 #my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
#my_cur.execute("SELECT * from fruit_load_list")
 #my_data_row = my_cur.fetchone()
#my_data_rows = my_cur.fetchall()
 #streamlit.text("Hello from Snowflake:")
 #streamlit.text("The fruit load list contains:")
 #streamlit.text(my_data_row)
#streamlit.header("The fruit load list contains:")
 #streamlit.dataframe(my_data_row)
#streamlit.dataframe(my_data_rows)
#Allow the end user to add a fruit to the list

#add_my_fruit = streamlit.text_input('What fruit would you like to add')
#streamlit.write('Thanks for adding ', add_my_fruit)
