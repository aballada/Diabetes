# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 11:11:21 2022

@author: ABalladaresO
"""

import streamlit as st
import joblib
import pandas as pd


model_filename = 'rf_model.pkl'
loaded_model = joblib.load(model_filename)
print("Modelo Cargado")


st.title('Status Diabetes')
st.header("Consulte su glucosa")
st.subheader("Ingrese los datos para su verificación")


with st.form(key='diabetes-pred-form'):
    col1, col2, col3, col4 = st.columns(4)
    Embarazo = col1.slider(label='Inserte número de embarazos:', min_value=0, max_value=20)
    Glucosa = col2.slider(label='Inserte glucosa:', min_value=50, max_value=400)
    Diastolica= col3.text_input(label='Inserte presión:')
    Grosor_piel = col4.text_input(label='Inserte grosor de piel:')


    col5, col6, col7, col8 = st.columns(4)
    Insulina = col5.slider(label='Inserte insulina:', min_value=20, max_value=400)
    BMI = col6.slider(label='Inserte BMI:', min_value=50, max_value=400)
    Diabete_pedigree= col7.text_input(label='Inserte diabete hereditaria:')
    age = col8.text_input(label='Inserte edad')
    
    submit = st.form_submit_button(label='Analizar')

    calculo = pd.DataFrame({'Embarazo': Embarazo, 'Glucosa': Glucosa, 'Diastolica': Diastolica, 'Grosor_piel': Grosor_piel, 'Insulina': Insulina, 'BMI': BMI, 'Diabete_pedigree': Diabete_pedigree, 'age': age }, index=[0])
    print(calculo)
    
    predicted_diabetes = loaded_model.predict(calculo)[0]
    st.write("El modelo estima que tiene diabetes: ",round(predicted_diabetes))

