import streamlit as st
from pathlib import Path

# Set paths
templates_dir = Path(__file__).parent / "templates"

# Read the HTML file
html_path = templates_dir / "index.html"
html_content = html_path.read_text()

# Render the HTML with Streamlit
st.set_page_config(page_title="Plate Mapper Tool", layout="wide")
st.components.v1.html(html_content, height=1000, scrolling=True)

