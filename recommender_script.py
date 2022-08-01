#Import 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import pickle as pkl

st.header("ADMISSION RECOMMENDATION SYSTEM")


model = pkl.load(open('model_pkl','rb'))
gender = st.sidebar.text_input('Input gender of applicant, either male or female')
ssc_p = st.sidebar.number_input('Input Secondary Education percentage- 10th Grade')
ssc_b = st.sidebar.text_input('Input Board of Education, either Central or Others')
hsc_p = st.sidebar.number_input('Input Higher Secondary Education percentage - 12th grade')
hsc_b = st.sidebar.text_input('Input Board of higher secondary education, either Central or others')
hsc_s = st.sidebar.text_input('Specialization in Higher Secondary Education, either Science, Commercial or Arts')
Degree_t = st.sidebar.text_input('Input Intended field of degree education, either Science,or Management, or others')

sex = None
if gender.lower() == 'male' :
    sex = 1
elif gender.lower() == 'female' :
    sex = 0
else :
    sex = "Incorrect Input"

sec = None
if ssc_b.lower() == 'central' :
    sec = 0
elif ssc_b.lower() == 'others' :
    sec = 1
else :
    sec = "Incorrect Input"

hsec = None
if hsc_b.lower() == 'central' :
    hsec = 0
elif hsc_b.lower() == 'others' :
    hsec = 1
else :
    hsec = "Incorrect Input"

hsec_s_science = None
hsec_s_Commercial = None
hsec_s_arts = None
if hsc_s.lower() == 'science' :
    hsec_s_science = 1
    hsec_s_Commercial = 0
    hsec_s_arts = 0
elif hsc_s.lower() == 'commercial' :
    hsec_s_science = 0
    hsec_s_Commercial = 1
    hsec_s_arts = 0
elif hsc_s.lower() == 'arts' :
    hsec_s_science = 0
    hsec_s_Commercial = 1
    hsec_s_arts = 0
else :
    hsec_s_science = "Invalid Input"
    hsec_s_Commercial = "Invalid Input"
    hsec_s_arts = "Invalid Input"

college_t_science = None
college_t_management = None
college_t_others = None
if  Degree_t.lower() == 'science' :
    college_t_science = 1
    college_t_management = 0
    college_t_others = 0
elif Degree_t.lower() == 'management' :
    college_t_science = 0
    college_t_management = 1
    college_t_others = 0
elif Degree_t.lower() == 'others' :
    college_t_science = 0
    college_t_management = 0
    college_t_others = 1
else :
    college_t_science = 'Invalid Input'
    college_t_management = 'Invalid Input'
    college_t_others = 'Invalid Input'

data = pd.DataFrame()
data['gender'] = [sex]
data['ssc_p'] = [ssc_p]
data['ssc_b'] = [sec]
data['hsc_p'] = [hsc_p]
data['hsc_b'] = [hsec]
data['hsc_s_Arts'] = [hsec_s_arts]
data['hsc_s_Commerce'] = [hsec_s_Commercial]
data['hsc_s_Science'] = [hsec_s_science]
data['degree_t_Comm&Mgmt'] = [college_t_management]
data['dagree_t_Others'] = [college_t_others]
data['degree_t_Sci&Tech'] = [college_t_science]

st.success("The data to use for prediction")

st.write(data)

st.success("Admission is recommended below")
if model.predict(data) == 1 :
    st.write("Hurray, The Candidate should be offered Admission")
else :
    st.write("The Candidate should try again next time")


st.success("Probability of the candidate gaining admission")
st.write(f'probability of gaining admission is {model.predict_proba(data)[:,1]}')