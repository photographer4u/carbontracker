import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Initialize session state for data storage
if 'data' not in st.session_state:
    st.session_state.data = pd.DataFrame(columns=['Activity', 'Carbon (kg)'])

if 'goals' not in st.session_state:
    st.session_state.goals = []

# Function to add new data
def add_data(activity, carbon):
    new_data = pd.DataFrame([[activity, carbon]], columns=['Activity', 'Carbon (kg)'])
    st.session_state.data = pd.concat([st.session_state.data, new_data], ignore_index=True)

# Function to add new goal
def add_goal(goal):
    st.session_state.goals.append(goal)

# Sidebar for data entry
st.sidebar.header('Data Entry')
activity = st.sidebar.text_input('Activity')
carbon = st.sidebar.number_input('Carbon (kg)', min_value=0.0)

if st.sidebar.button('Add Data'):
    add_data(activity, carbon)
    st.sidebar.success('Data added!')

# Sidebar for goal setting
st.sidebar.header('Set Goals')
goal = st.sidebar.text_input('Goal')

if st.sidebar.button('Add Goal'):
    add_goal(goal)
    st.sidebar.success('Goal added!')

# Main Dashboard
st.title('Digital Carbon Footprint Tracker')

# Data Visualization
st.header('Visualization')
if not st.session_state.data.empty:
    fig, ax = plt.subplots()
    st.session_state.data.plot(kind='line', x='Activity', y='Carbon (kg)', ax=ax)
    st.pyplot(fig)

# Data Reporting
st.header('Report')
st.write(st.session_state.data)

# Goal Display
st.header('Goals')
if st.session_state.goals:
    st.write(st.session_state.goals)
else:
    st.write("No goals set yet.")

# Total Carbon Calculation
st.header('Total Carbon Footprint')
total_carbon = st.session_state.data['Carbon (kg)'].sum()
st.write(f'Total Carbon Footprint: {total_carbon} kg CO2')
