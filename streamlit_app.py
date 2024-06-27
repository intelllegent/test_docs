import inspect
import textwrap

import plotly.express as px
import pandas as pd
import streamlit as st

st.set_page_config(layout="wide")

if "role" not in st.session_state:
    st.session_state.role = 'Analyst'

# Sidebar setup
docs = st.Page("docs.py", title="Documentation", icon=":material/description:")
dash = st.Page("dash.py", title="Dashboards", icon=":material/browse_activity:")

# Sidebar navigation
st.sidebar.title('Navigation')
role = st.sidebar.radio('Select role:', ['Analyst', 'Business'])
st.session_state.role = role

pg = st.navigation([docs, dash])
pg.run()
