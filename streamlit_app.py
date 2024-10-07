import streamlit as st

st.set_page_config(
    page_title="Abhay's Risk Analysis App",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'About': 'A personal project by abhaypai@vt.edu',
    }
)

input_page = st.Page(
    page = "Pages/1_Input.py",
    title = "Input",
    default = True
)

charts_page = st.Page(
    page = "Pages/2_Stock Charts.py",
    title = "Stock Charts"
)

risk_page = st.Page(
    page = "Pages/3_Risk Analysis.py",
    title = "Risk Analysis"
)

optimal_page = st.Page(
    page = "Pages/4_Optimal Portfolio.py",
    title = "Optimal Portfolio"
)


inputs=[input_page]
outputs=[charts_page, risk_page, optimal_page]

pg = st.navigation(
    {
        "User Input" : inputs,
        "Analyses" : outputs
    }
)

st.sidebar.text("Made by Abhay Pai")
st.sidebar.text("(@abhaypaii)")
pg.run()