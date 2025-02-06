import streamlit as st
import yfinance as yf
import datetime

st.header("Stock Market Analyzer")

#textbox for stock name
ticker_symbol=st.text_input("Enter Stock Symbol","AAPL", key="placeholder") #It will show the list of stock names
ticker_data=yf.Ticker(ticker_symbol) #data
#Getting date input
col1, col2 = st.columns(2)
with col1:
    st.header("Starting Date")
    start_date=st.date_input("Input Starting Date",datetime.date(2019,1,1))
with col2:
    st.header("Ending Date")
    end_date=st.date_input("Input Ending Date",datetime.date(2024,1,31))

ticker_df=ticker_data.history(period="1d",start=f"{start_date}",end=f"{end_date}")

dicter={"AAPL":"APPLE","GOOG":"GOOGLE"}

st.write(f"{dicter[ticker_symbol]} Stock Price Analysis")
st.dataframe(ticker_df)

col1, col2 = st.columns(2)
with col1:
    st.header("Volume Analysis")
    st.line_chart(ticker_df["Volume"])

with col1:
    st.header("Closing Price Analysis")
    st.line_chart(ticker_df["Close"])
