import streamlit as st
import time

# Page Config
st.set_page_config(page_title="A Message for You", page_icon="❤️")

# Custom CSS for a better look
st.markdown("""
    <style>
    .main { background-color: #fff5f5; }
    .stButton>button { width: 100%; border-radius: 20px; height: 3em; background-color: #ff4b4b; color: white; }
    h1 { color: #ff4b4b; text-align: center; }
    p { text-align: center; font-size: 1.2rem; }
    </style>
    """, unsafe_allow_html=True)

st.title("My care for you is real... ❤️")
st.write("Just like my mistake. I built this because a text wasn't enough.")

# Interactive Progress Bar
if st.button("Click to see how much I care for you"):
    progress_bar = st.progress(0)
    for percent_complete in range(100):
        time.sleep(0.01)
        progress_bar.progress(percent_complete + 1)
    st.success("Loading complete: 1,000,000% Care.")

# The Apology Logic
st.divider()
st.subheader("The Official Apology")
st.info("Beby's pookie is an idiot and sometimes forgets to take care of beby. Beby's pookie is very ashamed of himself and wants to make it up to beby. Beby's pookie loves beby very much and will do better in the future. Please forgive beby’s pookie for his mistakes. I always remember few lines from the song 'Shikayat': 'Suna hai ki unko shikayat bohot hai, to fir unko hamse mohhabat bhi bohot hai.'")

# The Forgiveness Button
col1, col2 = st.columns(2)

with col1: 
    if st.button("I Forgive You"):
        st.balloons()
        st.write("### ❤️ Best. News. Ever. ❤️")
        st.write("I'm counting down the days until I see you.")

# Footer
st.caption("Built with ❤️ and a bit of Python.")
