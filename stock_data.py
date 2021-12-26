import yfinance as yf
import streamlit as st
import pandas as pd
import csv
import csv

tickers = []
with open(r'nasdaq_screener_1640497257523.csv') as f:
    r = csv.reader(f)
    header = next(r)
    for row in r:
        tickers.append([row[1],row[0]])

tname = []
for i in tickers:
    tname.append(i[0])

st.write("""
# Simple Stock Price App

### Shows ***closing price*** and ***volume*** of Selected Company

***
""")

tickersymbol = ''

tickername = st.selectbox(
    'Select Ticker',
    tuple(tname))

for i in tickers:
    if i[0] == tickername:
        tickersymbol = i[1]

tickerdata = yf.Ticker(tickersymbol)

tickerdf = tickerdata.history(period='1d',start='2010-5-31',end='2020-5-31')

if not tickerdf.empty:
    st.write("""
    ## Closing Price
    """)
    st.line_chart(tickerdf.Close)
    st.write("""
    ## Volume Price
    """)
    st.line_chart(tickerdf.Volume)
else :
    st.error("No data found for this company")
    
st.write("""
***
""")