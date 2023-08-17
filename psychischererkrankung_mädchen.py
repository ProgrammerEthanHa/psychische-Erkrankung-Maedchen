import streamlit as st
import pandas as pd
import altair as alt

st.header("Psychische Erkrankungen bei Kindern & Jugendlichen (Mädchen)")
st.subheader("Prävelenz psychischer und Verhaltensstörung 2017 (Fälle je 1000)")

source = pd.DataFrame({
        ' ': [123.8, 85.0, 67.2, 14.9, 12.2, 16.2],
        'Erkrankung': ['Entwicklungsstörung', 'Verhaltens- und emotionale Störungen', 'Neurotische, Belastungs- und somatoforme Störungen', 'körperlichen Störungen', 'Persönlichkeits- und Verhaltensstörungen', 'Affektive Störungen']
     })
 
bar_chart = alt.Chart(source).mark_bar().encode(
        y=' :Q',
        x='Erkrankung:O',
    )
st.altair_chart(bar_chart, use_container_width=True)


txt = st.text_area('', '''
    Jugendlichen (0 bis 17); 2016/2017
    ''')
st.text("Klicke an die Balken um die Daten genauer anzuschauen. Du kannst auch die Diagramm vergrößern und ein Bild davon machen")
st.text("Quelle: DAK")