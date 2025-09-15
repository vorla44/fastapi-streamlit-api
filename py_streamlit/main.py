import streamlit as st
import requests

st.title(" Viestin lähetys FastAPI:lle")

#API_URL = "https://fastapi2-api.onrender.com/message"  # Vaihda tähän oma FastAPI-osoitteesi

API_URL = "http://localhost:8000/process/"
user_input = st.text_input("Kirjoita viesti FastAPI:lle:")

if st.button("Lähetä"):
    if user_input:
        try:
            response = requests.post(API_URL, json={"text": user_input})
            #st.write(type(response)) -> luokka
            #st.write(response) <Response [200]>
            if response.status_code == 200:
                st.success(f" Vastaus: {response.json()['processed_text']}")
                #response.json() = {'response':'Vastaanotettu viesti: kalle'}
            else:
                st.error(f" Virhe: {response.status_code}")
        except Exception as e:
            st.error(f"🔌 Yhteysvirhe: {e}")
    else:
        st.warning(" Kirjoita ensin viesti ennen lähettämistä.")