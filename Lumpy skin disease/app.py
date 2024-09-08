import streamlit as st
import numpy as np
import pandas as pd
import joblib 

IMAGE_SIZE = (180, 180)
THRESHOLD = 0.5

st.set_page_config(
    page_title="Lumpy Skin Disease",
    page_icon="👨‍⚕️"
)

st.header(':blue[Welcome to our Lumpy Skin Disease Prediction website.] :syringe: :pill: :ambulance:', divider='rainbow')



# with st.container(border=True):
placeholder = st.empty()
with placeholder.form("upload"):

    with st.container(border=True):
        st.header('Sample Data')
        st.text({'x': 0.555364, 'y': 0.634104, 'cld': 0.720365, 'dtr': 0.338710, 'frs': 0.397742, 'pet': 0.120000, 'pre': 0.303598, 'tmn': 0.713158, 'tmp': 0.708877, 'tmx': 0.677419, 'vap': 0.241259,
    'wet': 0.359314, 'elevation': 0.568306, 'dominant_land_cover': 0.181818, 'X5_Ct_2010_Da': 9.146893e-03,
    'X5_Bf_2010_Da': 0.000000e+00})

    st.markdown("<p style='text-align: center; color: grey;'>or</p>", unsafe_allow_html=True)


    with st.container(border=True):
        st.header(':yellow[Provide a csv data file]:mag:', divider='orange')
        uploaded_file = st.file_uploader("Upload a csv file", type=["jpg"])

    submit = st.form_submit_button("Predict")

    

if submit:
    if uploaded_file is None:
        placeholder.empty()

        model = joblib.load('./models/lumpy_model.sav')

        data = pd.DataFrame([[0.555364, 0.634104, 0.720365, 0.338710, 0.397742, 0.120000, 0.303598, 0.713158, 0.708877, 0.677419, 0.241259, 0.359314, 0.568306, 0.181818, 9.146893e-03, 0.000000e+00]])
        prediction = model.predict(data)

        if prediction[0]==1:
            st.header(f':mag: :rainbow[The COW is effeced with Lumpy skin disease virus.]')
        else:
            st.header(f':mag: :rainbow[The COW is not effeced with Lumpy skin disease virus.]')

    

