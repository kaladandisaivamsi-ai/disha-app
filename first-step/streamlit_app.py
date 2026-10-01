import streamlit as st
import streamlit.components.v1 as components

# Set page config for mobile-friendly view
st.set_page_config(
    page_title="Disha 2.0",
    page_icon="👩‍⚕️",
    layout="wide"
)

# Read your index.html file
try:
    with open("index.html", "r", encoding="utf-8") as f:
        html_content = f.read()
except FileNotFoundError:
    try:
        # Fallback if inside a subfolder
        with open("first-step/index.html", "r", encoding="utf-8") as f:
            html_content = f.read()
    except FileNotFoundError:
        st.error("Error: index.html file not found in the repository root or folder.")
        html_content = "<h1>Error: index.html missing</h1>"

# Render the HTML/JS application inside Streamlit with full responsive scrolling
components.html(html_content, height=900, scrolling=True)
