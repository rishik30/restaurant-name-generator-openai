import streamlit as st
import langchain_helper

st.title('Restaurant name generator')

cuisine = st.sidebar.selectbox('Pick a cuisine', ('Indian', 'Mexican', 'American', 'Italian'))

if cuisine:
  response = langchain_helper.generate_restaurant_name_and_items(cuisine)
  st.header(response['restuarant_name'].strip())
  menu_items = response['menu_items'].strip().split(',')
  st.write('Menu Items')
  for item in menu_items:
    st.write('-', item)
