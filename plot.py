import scipy
import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import plotly.express as px
import plotly.figure_factory as ff


# altair scatter plot:

chart_data=pd.DataFrame(np.random.randn(500,5),columns=['a','b','c','d','e'])

chart=alt.Chart(chart_data).mark_circle().encode(x='a',y='b',size='c',tooltip=['a','b','c','d','e'])
st.altair_chart(chart)

#interactive charts:

df=pd.read_csv('\\Users\\sumit\\Desktop\\streamlit\\lang_data.csv')
lang_list=df.columns.tolist()
lang_choices=st.multiselect('select your languages',lang_list)
new_df=df[lang_choices]
st.line_chart(new_df)

## area chart:
st.area_chart(new_df)

df=pd.read_csv('C:\\Users\\sumit\\Desktop\\streamlit\\tips.csv')
st.dataframe(df.head())

## pie chart:
fig=px.pie(df,values='total_bill',names='time')
st.plotly_chart(fig)

#piechart with multiple parameters:
fig=px.pie(df,values='total_bill',names='time',opacity=.3,color_discrete_sequence=px.colors.sequential.RdBu)
st.plotly_chart(fig)

## Histogram:
x1=np.random.randn(400)
x2=np.random.randn(400)
x3=np.random.randn(400)

hist_data=[x1,x2,x3]
group_labels=['Group-1','Group-2','Group-3']
fig=ff.create_distplot(hist_data,group_labels,bin_size=[.1,.25,.5])
st.plotly_chart(fig)
