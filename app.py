import streamlit as st
st.title("Ejemplo para usar session_state")

#si la etiqueta "count" no existe en la session state, se agregara la etiqueta "count" con un valor
if 'count' not in st.session_state:
    st.session_state['count'] = 0

if st.button('Click me'):
    st.session_state['count']+=1

st.write(st.session_state)
