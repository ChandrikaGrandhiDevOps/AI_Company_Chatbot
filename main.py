import streamlit as st
import langchain_helper

st.title("Company Name Generator")

cuisine = st.sidebar.selectbox("Company", ("Google","T-Mobile","Amazon", "ChurnPilot", "Udemy", "AT&T", "FedEX","UPs","Park University","Hospitals near me","Less Cost Cloths"))

if cuisine:
    response = langchain_helper.generate_company_name_and_services(cuisine)
    st.header(response['company_name'].strip())
    Services = response['Company'].strip().split(",")
    st.write("**Services**")
    for services in Services:
        st.write("-", services)

