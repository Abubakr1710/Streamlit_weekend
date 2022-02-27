import streamlit as st
import pandas as pd
#import matplotlib.pyplot as plt
#import seaborn as sns
#import plotly_express as px



sidebar = st.sidebar #no ()
TITLE = st.container()
datasection = st.container()
plotsection = st.container()

with sidebar:
    st.write('welcome to our project')
    st.title('main title')
    Box = st.selectbox('Which people do you want to choose', ('Peter', 'Abu', 'Busayo'))
    st.write('You selected:', Box)

with TITLE:
    st.title('Best Books')
    st.subheader('Here you can find best book to read')
    # st.header('header title')
    # st.subheader('header title')
    # st.markdown('* **header title** header title')
    # st.text('header title')
    st.subheader('---End of section---')


with datasection:
    st.subheader('something about best books to read')
    df = pd.read_csv('newdata.csv')
    df = df.loc[:, ~df.columns.str.contains('^Unnamed')] #toremove column'unnamed'
    st.write(df)    
    st.subheader('We have information of 1000 books in our data')

    st.subheader('---End of section---')

