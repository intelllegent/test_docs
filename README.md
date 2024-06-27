import streamlit as st
import plotly.express as px
import pandas as pd

df = pd.read_csv('data/dau.csv')

st.empty()
# Add a title and intro text
st.title('Метрики продуктовой команды DAU')

st.markdown("> **DAU** — количество уникальных девайсов, которые посещали страницу и взаимодействовали с контентом. Считается по наиболее сильному идентификатору пользователя (user_id)")
if st.session_state.role == 'Analyst':
    st.code("uniqIf(user_id, event in ('show', 'click', 'interact')) as dau")
with st.expander("Где посмотреть?"):
    fig = px.area(df, x="date_utc_mnt", y="DAU", color="group")
    st.plotly_chart(fig, theme=None, use_container_width=True)
    st.markdown("Ссылки на дашборды:")
    st.markdown('''
- [General](https://www.youtube.com/watch?v=oHg5SJYRHA0)
- [KPI](https://yandex.com)
    ''')
st.divider()

st.markdown("> **TimeSpent** — суммарное количество времени в секундах")
if st.session_state.role == 'Analyst':
    st.code("sum(total_duration_sec) as ts")
with st.expander("Где посмотреть?"):
    st.markdown('''
- Где-то
- Где-то еще
    ''')
st.divider()