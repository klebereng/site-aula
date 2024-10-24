# MEU PRIMEIRO WEB APP
import streamlit as st
  
# Use st.title("") para adicionar um TÍTULO ao seu Web app
st.title("Site para importar tabelas Exel ")

# Use st.header("") para adicionar um CABEÇALHO ao seu Web app
st.header("importar tabelas facil")

# Use st.subheader("") para adicionar um SUB CABEÇALHO ao seu Web app
st.subheader("Sub Cabeçalho")

# Use st.write("") para adicionar um texto ao seu Web app
st.write("Como já deve ter percebido, o método st.write() é usado para escrita de texto e informações gerais!")

import streamlit as st

col1, col2, col3 = st.columns(3)

with col1:
    st.header("Otavio Morale Faculdade")
    st.image("https://www.google.com/url?sa=i&url=https%3A%2F%2Fpt-br.facebook.com%2Fgroups%2F100616670283255%2Fpermalink%2F628679570810293%2F&psig=AOvVaw10O-UcDWR4Xq_DXBFCNApn&ust=1729818440501000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCNCdiv3ppYkDFQAAAAAdAAAAABAE")

with col2:
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg")

with col3:
    st.header("An owl")
    st.image("https://static.streamlit.io/examples/owl.jpg")
