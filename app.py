import streamlit as st

st.set_page_config(page_title = "🌱 Growth Mindset Challenge", layout= "centered")

st.markdown("""
<style>
            .stApp{
            background-image: linear-gradient(to right, #f9f9f9, #e0f7fa);
            color: #333;
            font-family: 'Segoe UI', sans-serif;
               h1, h2 {
        color: #2e7d32;
    }
    </style>}""", unsafe_allow_html=True)

# title and welcome
st.title("🌱 Growth Mindset Challenge✨")
st.header("Welcome to Your Growth Journey! 🚀")
st.write("Every step you take matters. Reflect, grow, and celebrate your wins with us today. ")

# Quote of the day
st.header("🌟Todays Growth Mindset Quote")
st.write("“Challenges are what make life interesting. Overcoming them is what makes life meaningful.” – Joshua Marine ")

#Challenge input
st.header("🧠 What's a Challenge you are facing Today?")
user_input = st.text_input("Share a challenge on your path:")

if user_input:
    st.success(f"You're working through: {user_input} 💪 Keep pushing forward — growth happens here!")
else:
    st.warning("Share your current challenge to start reflecting.")

#Reflection
st.header("📝 Reflect on Your Learning")
reflection = st.text_area("What did you learn today or recently?")

if reflection:
    st.success(f"🔍 Great insight! You reflected: _{reflection}_")
else:
    st.info("Taking a moment to reflect helps build a stronger mindset. Try it!")

# Achievement
    st.header("Celebrate a wins!")
    acheivement = st.text_input("Share something you've recently accomplished:")

    if acheivement:
        st.success(f"👏 Woohoo! You achieved: **{acheivement}** 🎯 Keep up the amazing work!")
    else:
        st.info("No win is too small. Share something you're proud of!")

st.write("- - -")
st.write("🌍 *Growth is a journey, not a destination. Keep believing in yourself — you’re doing great!*")
st.write("**✨ Created with ❤️ by Sanoober**") 

