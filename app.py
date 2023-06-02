import streamlit as st
import pandas as pd
import seaborn as sns

# Load the Iris dataset
iris_df = sns.load_dataset('iris')

# Set up the sidebar for interactive features
st.sidebar.header('Iris Dataset Visualization')
feature = st.sidebar.selectbox('Select a feature', iris_df.columns[:-1])

# Display the selected feature as a plot
st.subheader('Scatter plot of Iris dataset')
sns.scatterplot(data=iris_df, x='sepal_length', y='sepal_width', hue=feature)
st.pyplot()

# Display a histogram of the selected feature
st.subheader('Histogram of the selected feature')
sns.histplot(data=iris_df, x=feature, kde=True)
st.pyplot()
