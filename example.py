import streamlit as st
import pandas as pd

st.title('This is my website')

st.write('I love python')

file = st.file_uploader('Put a csv here')

try:
	df = pd.read_csv(file)
except:
	st.write('Where is the csv?')
else:
	if st.checkbox('Do you want to preview the dataframe?'):
		n_lines = int(st.number_input('How many lines do you want to see?',min_value = 1,step=1))
		selected_columns = df.columns
		selected_columns = st.multiselect('What columns do you want?', selected_columns)
		st.write(df.head(n_lines)[selected_columns])