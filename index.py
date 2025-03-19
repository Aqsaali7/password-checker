import re
import streamlit as st

# Page styling
st.set_page_config(page_title="Password strength with Aqsa Ali", layout="centered")
st.markdown("""
<style>
    .main {text-align: center;}
    .stTextInput {width: 60% !important; margin: auto;}
    .stButton button {width: 50%; background-color: #203823; color:black; font-size:18px;}
    .stButton button:hover {background-color: #27592D;}
</style>
""", unsafe_allow_html=True)

# Page title
st.title("Password Strength Generator")
st.write("Enter your password")

def check_password_strength(password):
    score = 0
    feedback = []

    # Check if the password length is at least 8 characters
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters.")
    
    # Check for both uppercase and lowercase letters
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Password should include both uppercase and lowercase letters.")

    # Check for at least one digit
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Password should include at least one digit.")

    # Check for special characters
    if re.search(r"[!@#$%&*]", password):
        score += 1
    else:
        feedback.append("❌ Password should include at least one special character.")

    # Display password strength
    if score == 4:
        st.success("Strong")
    elif score == 3:
        st.success("Risky")
    else:
        st.error(" 🕷️ Unsafe")    

    # Feedback
    if feedback:
        with st.expander("Improve your password"):
            for item in feedback:
                st.write(item)

# Get password input from user
password = st.text_input("Enter your password", type="password", help="Ensure your password is strong")

# Button
if st.button("Check strength"):
    check_password_strength(password)
else:
    st.warning("Please enter your password.")
