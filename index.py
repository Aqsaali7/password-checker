import re 
import streamlit as st

#page styling
st.set_config(page_title="Password strength with Aqsa Ali" , layout ="centered" )
st.markdown ("""
<style>
    .main {text-align: center};
    .stTextInput {width: 60% !important; margin: auto; }
    .stButton button {width: 50%; background-color: #203823; color:black; font-size:18px; }
    .stButton button:hover{ background-color:#27592D; }
<style>
""", unsafe_allow_html=True)

#PAGE TITLE
st.title("Password Strength Generator")
st.write("Enter your password")

def check_password_strength(password) :
    score = 0 
    feedback = [] 
     
     if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should aleast 8 character")
    
    if re.search (r"[A-Z]",) password amd re.search(r"[a-z]", password):
        score +=1
    else:
        feedback.append("❌ Password should inclued Both uppercase and lowercase")

    if re.search(r"\d", password):
        score +=1
    else:
         feedback.append("❌ Enter digits number")

#special character 
   if re.search(r"[!@#$%&*]" , password):
    score +=1
   else:
      feedback.append("❌ Enter some special character")

#display password strength      
    if score == 4:
    st.success ("Storng")
    elif score ==3:
        st.success("Risky")
    else:
        st.error(" 🕷️ Unsafe")    

 #feedback 
if feedback : 
    with st.expender("Improve your password"):
               for item in feedback:
                st.write(item)
password = st.text_input("Enter yoour password", type="password", help="Ensure your password is strong")

#Button
 if st.button("Check strength"):
    check_password_strength(password)
else:
    st.warning("Please enter your password")