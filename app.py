

import streamlit

streamlit.header('Breakfast Menu')
streamlit.text('Omega 3 & Blueberry Oatmeal')
streamlit.text('Kale, Spinach & Rocket Smoothie')
streamlit.text('Hard-Boiled Free-Range Egg')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
fruit_list=pandas.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
streamlit.dataframe(fruit_list)

fruit_list=fruit_list.set_index('Fruit')

fruit_selected=streamlit.multiselect('Pick some eFruit:', list(fruit_list.index),['Avocado','Strawberries'])
fruits_to_show=my_fruit_list.loc[fruit_selected]
#display

streamlit.dataframe(fruits_to_show)
