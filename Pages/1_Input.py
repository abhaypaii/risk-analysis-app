import streamlit as st
import pandas as pd
import yfinance as yf

c1, c2= st.columns([3,1], vertical_alignment="bottom")
with c1:
    st.title("Stock Portfolio Risk Evaluation")
with c2:
    st.page_link("Pages/2_Stock Charts.py", label="Go to Stock Charts →")

st.markdown("***Enter Stock tickers and their value in your portfolio***")

if 'portfolio' not in st.session_state:
        st.session_state.portfolio = pd.DataFrame({
            'Ticker': [''],
            'Value': [0.0]
        })

if 'file' not in st.session_state:
        st.session_state.file = pd.DataFrame({'Ticker': ['']})

# Function to add a new stock row
def add_stock():
    new_row = pd.DataFrame({
        'Ticker': [''],
        'Value': [0.0]
    })
    st.session_state.portfolio = pd.concat([st.session_state.portfolio, new_row], ignore_index=True)

rows = []
def remove_stock(index):
        st.session_state.portfolio = st.session_state.portfolio.drop(index).reset_index(drop=True)


# Create columns for buttons
for index, _ in st.session_state.portfolio.iterrows():
    col1, col2, col3 = st.columns([2, 1, 0.5], vertical_alignment="bottom")
    
    with col1:
        ticker = st.text_input(
            "Ticker",
            value=st.session_state.portfolio.at[index, 'Ticker'],
            key=f"ticker_{index}"
        )
        st.session_state.portfolio.at[index, 'Ticker'] = ticker

    with col2:
        value = st.number_input(
            "Value (in $)",
            min_value=0.0,
            value=float(st.session_state.portfolio.at[index, 'Value']),
            format="%.2f",
            key=f"Value_{index}"
        )
        st.session_state.portfolio.at[index, 'Value'] = value

    with col3:
        if index > 0:  # Don't allow removing the first row
            if st.button("🗑️", key=f"remove_{index}"):
                remove_stock(index)
                st.rerun()

st.session_state.portfolio = pd.DataFrame(st.session_state.portfolio)

    
col1, col2 = st.columns([1, 3])
with col1:
    add_stock_button = st.button("Add Another Stock", on_click=add_stock)



