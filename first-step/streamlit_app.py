import streamlit as st
import streamlit.components.v1 as components

# Set page config
st.set_page_config(
    page_title="Disha 2.0 - AI Mode",
    page_icon="👩‍⚕️",
    layout="wide"
)

st.sidebar.title("🔐 Configuration")
api_key = st.sidebar.text_input("Enter Gemini API Key", type="password")

if not api_key:
    st.sidebar.warning("Please enter your API key to activate live AI answers.")

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

# Inject the API key into the HTML environment if provided
if api_key:
    # Inject script setting the API key globally in the browser window session
    inject_script = f"<script>window.GEMINI_API_KEY = '{api_key}';</script>"
    html_content = html_content.replace("</head>", f"{inject_script}</head>")

# Render the HTML application inside Streamlit
components.html(html_content, height=900, scrolling=True)
