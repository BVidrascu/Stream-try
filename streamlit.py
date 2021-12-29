import streamlit as st
import pandas as pd

data = pd.read_csv('https://raw.githubusercontent.com/BVidrascu/Stream-try/main/survey_results_public.csv')
header = st.container()
body = st.container()

with header:
    st.title('Bine ai venit, prost ai nimerit')
    st.text('Aici o sa vezi si nu o sa crezi, crede-ma pe mine bro')

with body:
    st.text('Hai prima data sa vedem cu ce lucram!')
    st.write(data.head())
    st.text('Destul de nice, nu?\nAnyways, uite un chart care arata distributia adeptilor culturii open source dintre respondenti')
    opsrc_distribution = pd.DataFrame(data['OpenSourcer'].value_counts())
    st.bar_chart(opsrc_distribution, height = 700, width = 1000)
    x = st.slider('Cat de mult ti-a placut?', 1, 10, 0)  
    st.write('Ok, ', x, ' sa fie, daca atata vrei tu...')
    buton = st.button('Nu apasa butonul')
    st.write(buton)
    if buton:
        st.balloons()

    
