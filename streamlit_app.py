import pandas as pd
import streamlit as st
from numpy.random import default_rng as rng

st.title("Hello, Streamlit!")
st.header("This is a header with a divider", divider="rainbow")

with st.sidebar:
    st.header("About app")
    st.write("This is my first Streamlit app!")

st.markdown("*Streamlit* is **really** ***cool***.")

st.subheader("st.column")

col1, col2 = st.columns(2)

with col1:
    x = st.slider("Choose an x value", 1, 10)
with col2:
    st.write("The value fo :blue[***x***] is:", x)

st.markdown("Here's a bouquet &mdash;\
            :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")

df = pd.DataFrame(rng(0).standard_normal((20, 3)), columns=["a", "b", "c"])

st.area_chart(df)
