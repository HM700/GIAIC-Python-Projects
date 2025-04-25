
import streamlit as st
import re

st.set_page_config(page_title="Password Strength Checker", page_icon="🔒")

st.title("💪 Password Strength Checker")
st.markdown("### Welcome to the ultimate password strength checker! Use this tool to check the strength of your password.")

# Input field for password
password = st.text_input("Enter Your Password", type="password")

feedback = []
score = 0

if password:
    # Check length
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("🔸 Password should be at least 8 characters long.")

    # Check for both uppercase and lowercase characters
    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("🔸 Password should contain both uppercase and lowercase letters.")

    # Check for digits
    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append("🔸 Password should contain at least one digit.")

    # Check for special characters
    if re.search(r'[@!#$&*]', password):
        score += 1
    else:
        feedback.append("🔸 Password should contain at least one special character (@!#$&*).")

    # Show strength result
    if score == 4:
        st.success("✅ Your password is strong 💪")
    elif score == 3:
        st.warning("⚠️ Your password is of medium strength.")
    else:
        st.error("❌ Your password is weak. Please make it stronger.")

    # Show suggestions
    if feedback:
        st.markdown("## 🔧 Improvement Suggestions")
        for tip in feedback:
            st.write(tip)

else:
    st.info("🔐 Please enter your password to get started.")
