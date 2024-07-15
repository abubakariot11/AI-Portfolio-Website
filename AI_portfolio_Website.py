import streamlit as st
import google.generativeai as genai

# Configure the Google API key
genai.configure(api_key="AIzaSyCmtT3xyOq6KQMGfsjp-KfgAa_xo2DcDvg")
model = genai.GenerativeModel('gemini-1.5-flash')

# Custom CSS for background image
page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("https://img.freepik.com/free-vector/stream-binary-code-design_53876-118375.jpg");
background-size: 120%;
}}
</style>
"""

# Inject the CSS
st.markdown(page_bg_img, unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.subheader("Hi :wave:")
    st.title("I am Muhammad Abubakar Raza")
    st.write("Associate Engineer of Internet of things | Python Developer")

with col2:
    st.image("D:/Python_and_computer_vision_bootcamp/chapter 04/images/Abu bakar.jpg")

st.title(" ")

persona = """
        You are Abubakar AI bot. You help people answer questions about yourself (i.e. Muhammad Abubakar Raza). Answer as if you are responding.
        Don't answer in the second or third person. If you don't know the answer, simply say, 
        "That's a secret."
         
    Here is more info about Muhammad Abubakar Raza:
     
    Muhammad Abubakar Raza is an Associate Engineer specializing in Internet of Things (IoT) and Python Development. Based in Lahore, Punjab, Pakistan, 
    he is passionate about education and technology. 
    He was studying at Punjab University Lahore and was an advanced electronics and PCB designer. he now focuses on educating and inspiring others.

    Abubakar is  Diploma Holder with a Diploma of Associate Engineering in Internet of Things and Application Technology from ATIN NLC Mandra. 
    He has completed courses and projects with FreeCodeCamp and WsCubeTech, enhancing his expertise in various technologies including Python, 
    Data Structures and Algorithms (Java), Web Development, CVzone Compter Vission,
    (NodeJs, MySQL), Android Studio, and Machine Learning (Python).

    His experience includes working as machine Learning Engineer at WsCubeTech, an Android Studio Programmer at WsCubeTech and as a Backend Developer at FreeCodeCamp, and as a Python Developer, Web Developer, SQL DataBase at Arfa Karim Softare technology Park Lahore 
    Abubakar is dedicated to continuous learning and innovation in tech. Beyond his professional life, he enjoys tea, acting, and theater.

    Some of his notable projects are:
    - Crafting Engaging Stories with AI
    - AI for Everyone
    - Assessing Water Quality for Irrigation
    - Gemini AI Projects with Python
    - Streamlit AI Apps
    - WhatsApp ChatBot using OpenAI
    - Image to Text
    - CV Zone Projects
    - ChatGPT All Models in Python
    - LLM (Large Language Model) Lama

    You can explore his projects further on his GitHub: https://github.com/abubakariot11


        Abubakar's Email: mabubakarraza11@gmail.com
        Abubakar's Linkdin: https://www.linkedin.com/in/muhammad-abubakar-raza-084885263/
        Abubakar's Github :https://github.com/abubakariot11
        """

st.title('🤖'  "Abubakar's AI Bot")

user_question = st.text_input("Ask anything about me")
if st.button("ASK", use_container_width=400):
    prompt = persona +"Here is the question that the user asked: " +  user_question
    response = model.generate_content(prompt)
    st.write(response.text)

st.title(" ")

col1, col2 = st.columns(2)
with col1:
    st.subheader('📹'"Youtube Channel")
    st.write("- Robotics and CVzone")
    st.write("- 9.98K subscribers")
    st.write("- 351 videos")
    st.write("- 1.03 million views")

with col2:
    st.video("https://youtu.be/6VTQwAfN6oQ?si=z0Cq2cq_WWfvDTdI")

st.title(" ")

st.title('⚙️'"My Setup")
st.image("D:/Python_and_computer_vision_bootcamp/chapter 04/images/image.jpg")

st.write(" ")
st.title('👩‍💻'"My Skills")
st.slider("Programming", 0, 100, 80)
st.slider("Researhing and Developments", 0, 100, 75)
st.slider("Electronics & Robotics", 0, 100, 90)
st.slider("Computer-aided design", 0, 100, 70)

st.write(" ")
st.title('📷'"My Projects Gallery")

col1, col2, col3 = st.columns(3)

with col1:
    st.image("D:/Python_and_computer_vision_bootcamp/chapter 04/images/g1.png")
    st.image("D:/Python_and_computer_vision_bootcamp/chapter 04/images/g2.png")
    st.image("D:/Python_and_computer_vision_bootcamp/chapter 04/images/g3.jpg")

with col2:
    st.image("D:/Python_and_computer_vision_bootcamp/chapter 04/images/g4 (2).jpg")
    st.image("D:/Python_and_computer_vision_bootcamp/chapter 04/images/g5.png")
    st.image("D:/Python_and_computer_vision_bootcamp/chapter 04/images/g6.jpg")

with col3:
    st.image("D:/Python_and_computer_vision_bootcamp/chapter 04/images/g7.jpg")
    st.image("D:/Python_and_computer_vision_bootcamp/chapter 04/images/g8.jpg")
    st.image("D:/Python_and_computer_vision_bootcamp/chapter 04/images/g9.jpg")

st.subheader(" ")
st.write("CONTACT")
st.title("Get in touch with me if you have any queries")
st.subheader('📧'"mabubakarraza11@.com")
st.subheader("www.linkedin.com/in/muhammad-abubakar-raza-084885263/")
st.icon = "fa-envelope"