import os
import streamlit as st
from exa_py import Exa
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Exa API
exa_api_key = os.getenv('EXA_API')
if exa_api_key is None:
    st.error('EXA_API key not found. Please set it in the .env file.')
else:
    exa = Exa(api_key=exa_api_key)

# Streamlit interface
st.title('SnapSearch ✦.')
st.subheader('Search any content with SnapSearch ')
domain = st.text_input('Enter the URL of the Social Media platform where you want to search: (e.g., https://medium.com/, https://www.reddit.com/)')
query = st.text_input('Search your content here: (e.g., Resume building tips by coding content creators, WEB3 creators)')

if st.button('Search'):
    if not domain:
        st.warning('Please enter a URL for the Social Media platform.')
    elif not query:
        st.warning('Please enter a content.')
    else:
        response = exa.search(
            query,
            num_results=10,
            type='keyword',
            include_domains=[domain],
        )
    
        st.subheader(f'Search results for: {query}')
        if response.results:
            for result in response.results:
                st.write(f"**Title:** {result.title}")
                st.write(f"**URL:** {result.url}")
                st.write("---")
        else:
            st.write('No results found.')
