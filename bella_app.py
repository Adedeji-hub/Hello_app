import streamlit as st

#Title and Text:
#Title:
st.title('My Streamlit App')
#--------------------------------------------------------
#Header and Subheader:
st.header('Header')
st.subheader('Subheader')
#--------------------------------------------------------
#Text:
st.write('This is a simple text.')
#--------------------------------------------------------
#--------------------------------------------------------

#Widgets:
#Text Input:
user_input = st.text_input('Enter your name:', 'Default Name')
#--------------------------------------------------------
#Slider:
age = st.slider('Select your age:', 0, 100, 25)
#--------------------------------------------------------
#Button:
if st.button('Submit'):
    st.write(f'You clicked the button!')
#--------------------------------------------------------
#Checkbox:
if st.checkbox('Show Data'):
    st.write('Here is your data.')