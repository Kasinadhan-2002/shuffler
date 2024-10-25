import streamlit as st
import random

# Initialize session state variables
if 'names' not in st.session_state:
    st.session_state.names = []
if 'shuffled_names' not in st.session_state:
    st.session_state.shuffled_names = []

# Function to reset the list and shuffle the names again
def reset_names():
    st.session_state.shuffled_names = st.session_state.names[:]
    random.shuffle(st.session_state.shuffled_names)

# Function to delete a name
def delete_name(name):
    if name in st.session_state.names:
        st.session_state.names.remove(name)
        reset_names()  # Reshuffle the names
def remove_duplicates():
    st.session_state.names = list(set(st.session_state.names))
    reset_names()

# App title
c1,center,c2 = st.columns([1.5,3,1.5])
center.title("Random Picker")

# Input field to add multiple names (comma-separated)
name_input = st.text_area("Enter the data (comma-separated):")

# Add names button
if st.button("Add"):
    if name_input.strip():
        # Split the input by commas and strip any extra whitespace
        names_to_add = [name.strip() for name in name_input.split(',') if name.strip()]
        st.session_state.names.extend(names_to_add)
        remove_duplicates()  # Remove duplicates after adding new names
        reset_names()  # Shuffle the names
        st.success(f"Datas '{', '.join(names_to_add)}' added!")
    else:
        st.warning("Please enter a valid data.")

# Display current shuffled names
if st.session_state.names:
    st.subheader("Current Shuffled List:")
    st.write(st.session_state.shuffled_names)
    st.subheader("Options:")

    # Pick a random name button
    if st.button("Pick a Random Data"):
        if st.session_state.shuffled_names:
            random_name = random.choice(st.session_state.shuffled_names)
            st.success(f"Random Data Picked: {random_name}")
        else:
            st.warning("No data available to pick from.")
        
        
    # Option to delete a name    
    if st.session_state.names:
        name_to_delete = st.selectbox("Select a data to delete:", st.session_state.names)
        row1,row2,blank = st.columns([0.7,1,4])        
        if row1.button("Delete"):
            delete_name(name_to_delete)
            st.success(f"Data '{name_to_delete}' deleted!")
    else:
        row1,row2,blank = st.columns([0.7,1,4])        
        row2.info("No data available to delete.")
        
    # Reset button to reset and reshuffle the names
    if row2.button("Reset"):
        reset_names()
        st.info("Data have been reset and reshuffled.")

else:
    st.info("No values added yet. Please add data to start.")
