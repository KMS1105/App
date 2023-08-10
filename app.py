import streamlit as st
import time

"""https://www.youtube.com/watch?v=8u2PngR2xpM, Terminal=streamlit run (File Path)"""

tab1, tab2= st.tabs(['Tab A' , 'Tab B'])  

with tab1:
    st.title("Test") 
    
    with st.form("form1"):
        In = st.text_input(label="In", max_chars=10)
        submit = st.form_submit_button("Submit")


    if In and submit:
        with st.spinner("Saving..."):
            time.sleep(0.1)
            st.write("Save!")
            time.sleep(0.1)
      
    with tab2:   
        st.title("Test") 
                
                

