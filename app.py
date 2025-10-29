import streamlit as st
st.title("Ejemplo para usar session_state")

if 'name' not in st.session_state:
    st.session_state['name']= ''
    
#si la etiqueta "count" no existe en la session state, se agregara la etiqueta "count" con un valor
if 'count' not in st.session_state:
    st.session_state['count'] = 0

if st.button('Click me'):
    st.session_state['count']+=1
    
nombre = st.text_input("Escribe tu nombre")
st.write(nombre)

if nombre:
    st.session_state['name']+=nombre


st.write(st.session_state)
