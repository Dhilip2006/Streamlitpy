import streamlit as st
st.title("Basic Calculator")
st.write("""1. Addition
            2. Subtraction
            3. Multiplication
            4. Division
            5. Exponent
            6. Modulus
            7. Floor Division""")
choice = st.number_input("Enter a Choice", value=0)
num_1 = st.number_input("Enter a Number 1")
num_2 = st.number_input("Enter a Number 2")
if st.button("click here"):
   if(choice == 1):
      st.write("Addition")
      st.write(num_1 + num_2)
   elif(choice == 2):
      st.write("Subtraction")
      st.write(num_1 - num_2)
   elif(choice==3):
      st.write("Multiplication")
      st.write(num_1*num_2)
   elif(choice==4):
      st.write("Division")
      st.write(num_1/num_2)
   elif(choice==5):
      st.write("Exponent")
      st.write(num_1**num_2)
   elif(choice==6):
       st.write("Modulus(Remainder)")
       st.write(num_1%num_2)
   elif(choice==7):
      st.write("Floor Division")
      st.write(num_1//num_2)
   else:
      st.write("Invalid Choice")
