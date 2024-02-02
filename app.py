import streamlit as st
from datetime import datetime
import pytz
import time

# Function to display the world clock page
def world_clock_page():
    st.title('World Clock')

    time_zones = list(pytz.all_timezones)

    if 'selected_locations' not in st.session_state:
        st.session_state.selected_locations = ["US/Pacific"]

    # Selection limit
    def limit_selection():
        if len(st.session_state.selected_locations) > 4:
            # If more than 4 locations are selected, show a warning and revert to the last valid selection
            st.warning('You can select up to 4 locations only.')
            st.session_state.locations = st.session_state.locations[:4]

    # Enforce the selection limit
    locations = st.multiselect(
        'Select up to 4 locations',
        time_zones,
        default=st.session_state.selected_locations,
        on_change=limit_selection,
        key='locations'
    )

    # Update session state
    st.session_state.selected_locations = locations

    # Function to display times for selected locations
    def display_times(locations):
        for location in locations:
            # Get the current time in the selected time zone
            tz = pytz.timezone(location)
            current_time = datetime.now(tz)
            formatted_time = current_time.strftime('%Y-%m-%d %H:%M:%S')

            # Calculate UNIX timestamp
            # Convert the time to UTC before getting the timestamp to ensure consistency
            utc_time = current_time.astimezone(pytz.utc)
            unix_timestamp = int(utc_time.timestamp())

            # Display the location, its current time, and the UNIX timestamp
            st.subheader(f"{location} Time")
            st.write(f"Current Time: {formatted_time}")
            st.write(f"UNIX Timestamp: {unix_timestamp}")

    # Display the times for the selected locations
    display_times(locations)
    # Re-run the app every second to update the times
    st.experimental_rerun()






# Function to display the timestamp converter page
def timestamp_converter_page():
    st.title('Timestamp Converter')
    timestamp_input = st.number_input(
        'Enter UNIX timestamp:',
        value=int(time.time()),
        format='%d'
    )

    # Convert UNIX timestamp to human-readable time
    human_time = datetime.utcfromtimestamp(timestamp_input).strftime(
        '%Y-%m-%d %H:%M:%S UTC'
    )
    st.write(f"Human-readable time: {human_time}")




# Sidebar for navigation
page = st.sidebar.selectbox("Choose a page", ["World Clock", "Timestamp Converter"])


# Page rendering
if page == "World Clock":
    world_clock_page()
elif page == "Timestamp Converter":
    timestamp_converter_page()
