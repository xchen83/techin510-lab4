import pytz
import streamlit as st
from datetime import datetime

# List of time zones for the dropdown menu
time_zones = list(pytz.all_timezones)

# Streamlit UI components
st.title('World Clock App')
selected_zones = st.multiselect('Select Locations', time_zones, default=['UTC'])

# Display current time for each selected time zone
for zone in selected_zones:
    now = datetime.now(pytz.timezone(zone)).strftime('%Y-%m-%d %H:%M:%S')
    st.subheader(f"{zone}: {now}")

# JavaScript to trigger auto-refresh
refresh_rate = 1000  # Refresh rate in milliseconds
st.markdown(f"""
    <script>
    setInterval(function() {{
        window.location.reload();
    }}, {refresh_rate});
    </script>
    """, unsafe_allow_html=True)