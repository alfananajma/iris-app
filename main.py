import pickle
import streamlit as st
import numpy as np

st.title("Flowers Classification App")

with open("best_model.pkl","rb") as f:
    lr_model = pickle.load(f)

s1 = st.number_input("insert a sepal length")
sw = st.number_input("insert a sepal width")
pl = st.number_input("insert a petal length")
pw = st.number_input("insert a petal width")

if st.button("predict"):
    pred = lr_model.predict(np.array([[sl,sw,pl,pw]]))
    st.write("the flower is :", pred[0])