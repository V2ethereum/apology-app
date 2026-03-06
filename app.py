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

st.title("Distance is just a number... ❤️")
st.write("But my mistake was real. I built this because a text wasn't enough.")

# Interactive Progress Bar
if st.button("Click to see how much I miss you"):
    progress_bar = st.progress(0)
    for percent_complete in range(100):
        time.sleep(0.01)
        progress_bar.progress(percent_complete + 1)
    st.success("Loading complete: 1,000,000% Missed.")

# The Apology Logic
st.divider()
st.subheader("The Official Apology")
st.info("beby's pookie knows that he messed up. he is sorry for not taking care of you and kept talking like an idiot. beby's pookie is working on being better for us.")

# The Forgiveness Button
col1, col2 = st.columns(2)

with col1:
    if st.button("I Forgive You"):
        st.balloons()
        st.write("### ❤️ Best. News. Ever. ❤️")
        st.write("I'm counting down the days until I see you.")

with col2:
    if st.button("I need more snacks first"):
        st.warning("Order placed! 🍫 Check your DoorDash/UberEats soon!")
        st.write("*(But seriously, I love you)*")

# Footer
st.caption("Built with ❤️ and a bit of Python.")
