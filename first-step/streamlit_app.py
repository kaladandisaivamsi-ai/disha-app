import streamlit as st
import streamlit.components.v1 as components

# Set page config for mobile-friendly view
st.set_page_config(
    page_title="Disha 2.0",
    page_icon="👩‍⚕️",
    layout="centered"
)

# Read your index.html file
try:
    with open("index.html", "r", encoding="utf-8") as f:
        html_content = f.read()
except FileNotFoundError:
    try:
        with open("first-step/index.html", "r", encoding="utf-8") as f:
            html_content = f.read()
    except FileNotFoundError:
        html_content = "<h1>Error: index.html missing</h1>"

# Render the HTML/JS application inside Streamlit cleanly
components.html(html_content, height=850, scrolling=True)
