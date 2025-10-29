import streamlit as st
st.title("Ejemplo para usar session_state")

#si la etiqueta "count" no existe en la session state, se agregara la etiqueta "count" con un valor
if 'count' not in st.session_state:
    st.session_state['count'] = 0

if 'name' not in st.session_state:
    st.session_state['name']=''

if st.button('Click me'):
    st.session_state['count']+=1

name=st.text_input("escribe tu nombre")
st.write(name)

st.write(st.session_state)
