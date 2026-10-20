
import streamlit as st

st.set_page_config(page_title="Off-by-Three AI Hackathon")

st.title("Off-by-Three AI Hackathon")
st.write("Welcome to our project!")

st.subheader("Project Notes")
notes = st.text_area("Enter your notes here:")

if st.button("Generate"):
    if notes.strip():
        st.success("Your notes have been submitted!")
        st.write(notes)
    else:
        st.warning("Please enter some notes first.")
