import streamlit as st
from datetime import datetime
import pytz

# List of time zones for the dropdown
time_zones = list(pytz.all_timezones)

# Streamlit UI for selecting locations
st.title('World Clock')
locations = st.multiselect('Select up to 4 locations', time_zones, default=["UTC"])

# Function to display times for selected locations
def display_times(locations):
    for location in locations:
        # Get the current time in the selected time zone
        current_time = datetime.now(pytz.timezone(location)).strftime('%Y-%m-%d %H:%M:%S')
        # Display the location and its current time
        st.subheader(f"{location} Time")
        st.write(current_time)

# Display the times initially
display_times(locations)

# Rerun the script every second to update the times
st_autorefresh = st.sidebar.slider('Refresh every x seconds', min_value=1, max_value=10, value=1)
st.button("Refresh Now")

st.experimental_rerun()
