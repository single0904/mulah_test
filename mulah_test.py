import csv
import streamlit as st
import pandas as pd
import numpy as np


st.write("""
# Mulah Test
Table 1
""")

data = pd.read_csv('Table_Input.csv')

df = pd.DataFrame(data)

st.table(df)

st.write("""
Table 2
""")

values = data.values
alphaVal = 0
betaVal = 0
charlieVal = 0

for i in range(len(values)):
    if (values[i][0] == 'A5'):
        alphaVal = values[i][1]
    if (values[i][0] == 'A13'):
        charlieVal = values[i][1]
    if (values[i][0] == 'A15'):
        betaVal = values[i][1]

for i in range(len(values)):
    if (values[i][0] == 'A7'):
        betaVal = betaVal / values[i][1]
    if (values[i][0] == 'A12'):
        charlieVal = charlieVal * values[i][1]
    if (values[i][0] == 'A20'):
        alphaVal += values[i][1]

table2Header = ['Category', 'Value']
table2Val = [['Alpha', alphaVal], ['Beta', betaVal], ['Charlie', charlieVal]]

df2 = pd.DataFrame(table2Val,columns = table2Header)

st.table(df2)

