import streamlit as st
x = st.number_input("Enter first number: ")
y = st.number_input("Enter second number: ")
z = st.number_input("Enter third number: ")
if (x >= y) and (x >= z):
  largest = x
elif (y >= x) and (y >= z):
  largest = y
else:
  largest = z
st.write("largest number is: ", largest)
