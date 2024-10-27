import streamlit as st
st.title(" My Portfolio")
st.subheader("About Me")
import streamlit as st

# Set the title of the app
st.title("My Portfolio")

# Add a brief introduction
st.write("""
Hello! I'm Dhilip, a passionate of Programming and Data analysis with experience in some competition.
Below are some of my projects that I'm proud to showcase.
""")

# Project 1
st.subheader("Project 1: Python competetion")
st.image("https://www.androidgame365.com/puzzle/11370-hand-cricket.html", caption="Project 1 Screenshot", use_column_width=True)
st.write("""
Description: A brief description of your project. What it does, technologies used, etc.
""")
# Project 2
st.subheader("Project 2: Basic calculator")
st.write("""
Description: A brief description of your project. What it does, technologies used, etc.
""")
st.image("https://www.google.com/imgres?q=basic%20calculator%20photos&imgurl=https%3A%2F%2Fauthorguide.learnosity.com%2Fhc%2Farticle_attachments%2F5711467221405%2FBasicCalculator.png&imgrefurl=https%3A%2F%2Fauthorguide.learnosity.com%2Fhc%2Fen-us%2Farticles%2F360000657178-Using-the-Calculator-with-Simple-Features&docid=nRcFbK2uf01LmM&tbnid=ZFjf6S0F-iltnM&vet=12ahUKEwj1tvfLlayJAxV01TgGHUcXOKcQM3oECF4QAA..i&w=566&h=904&hcb=2&ved=2ahUKEwj1tvfLlayJAxV01TgGHUcXOKcQM3oECF4QAA", caption="Project 2 Screenshot", use_column_width=True)
st.markdown("[View Project](http://link_to_your_project2.com)")
# Contact Information
st.header("Contact Me")
st.write("Feel free to reach out via:")
st.write("- Email: your_email@example.com")
st.write("- LinkedIn: [Your LinkedIn Profile](http://link_to_your_linkedin_profile.com)")