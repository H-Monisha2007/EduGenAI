import streamlit as st
from datetime import datetime

st.set_page_config(page_title="EduGenAI", layout="centered")

st.title("🎓 EduGenAI")
st.subheader("Personalized Generative AI Learning & Career Assistant")

st.markdown("⚡ *LLM Integration ready for deployment*")

st.divider()

# -----------------------
# User Inputs
# -----------------------
goal = st.text_input("🎯 Enter Your Goal (e.g., Data Scientist)")
level = st.selectbox("📘 Select Your Level", ["Beginner", "Intermediate", "Advanced"])
topic = st.text_input("📚 Topic You Want to Learn")

st.divider()

# -----------------------
# Generate Learning Path
# -----------------------
if st.button("🚀 Generate Learning Path"):

    if goal and topic:

        st.success("Learning Path Generated Successfully!")

        st.markdown("## 📍 Step-by-Step Roadmap")

        if level == "Beginner":
            st.write("1. Understand basic concepts of", topic)
            st.write("2. Learn fundamental tools and terminology")
            st.write("3. Practice with beginner-friendly projects")
            st.write("4. Explore real-world use cases")
        elif level == "Intermediate":
            st.write("1. Strengthen core concepts of", topic)
            st.write("2. Work on dataset-based projects")
            st.write("3. Learn advanced tools and frameworks")
            st.write("4. Prepare for job-level problem solving")
        else:
            st.write("1. Master advanced concepts of", topic)
            st.write("2. Build scalable production-level projects")
            st.write("3. Optimize performance & architecture")
            st.write("4. Prepare for technical interviews")

        st.markdown("## 💼 Suggested Projects")
        st.write("- Mini Project related to", topic)
        st.write("- Real-world case study")
        st.write("- Portfolio-ready implementation")

        st.markdown("## 🎤 Interview Preparation")
        st.write("- Explain core concepts of", topic)
        st.write("- Scenario-based problem solving")
        st.write("- Practical application questions")

        st.markdown("## 📄 Resume Tip")
        st.info(f"Highlight projects in {topic} aligned with your goal: {goal}")

    else:
        st.error("Please fill all fields!")

st.divider()

# -----------------------
# Quiz Generator
# -----------------------
if st.button("📝 Generate Practice Quiz"):
    if topic:
        st.markdown("## 🧠 Practice Questions")
        st.write(f"1. What are the key concepts of {topic}?")
        st.write(f"2. Explain real-world applications of {topic}.")
        st.write(f"3. What tools are commonly used in {topic}?")
        st.write("4. Describe challenges and solutions.")
    else:
        st.error("Please enter a topic first!")

st.divider()

st.caption("© 2026 EduGenAI | Prototype Version | Powered by Simulated AI")