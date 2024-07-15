import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Title of the dashboard
st.title('타이타닉 생존자 예측하기')

titanic = pd.read_csv("./data/titanic.csv")
st.dataframe(titanic)

f,ax=plt.subplots(1,2,figsize=(18,8))
data['Survived'].value_counts().plot.pie(explode=[0,0.1],autopct='%1.1f%%',ax=ax[0],shadow=True)

ax[0].set_title('Survived')
ax[0].set_ylabel('')
sns.countplot(x='Survived', data=data, ax=ax[1])
ax[1].set_title('Survived')
plt.show()

# Sidebar for user input
st.sidebar.header('User Input Parameters')
n = st.sidebar.slider('Number of data points', 10, 100, 50)
option = st.sidebar.selectbox('Select a chart type', ('Line Chart', 'Bar Chart'))

# Generate random data
data = pd.DataFrame({
    'x': np.arange(n),
    'y': np.random.randn(n).cumsum()
})

# Display the data
st.write('### Generated Data', data)

# Plot the data
st.write('### Chart')
if option == 'Line Chart':
    st.line_chart(data.set_index('x'))
elif option == 'Bar Chart':
    fig, ax = plt.subplots()
    ax.bar(data['x'], data['y'])
    st.pyplot(fig)

# Adding a map
st.write('### Map')
map_data = pd.DataFrame(
    np.random.randn(100, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])
st.map(map_data)

