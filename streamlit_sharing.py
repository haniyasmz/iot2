'''
Created on 12 Jan 2023

@author: hanimurnizam
'''

import streamlit as st
import pandas as pd
import psycopg2
# from sqlalchemy import create_engine
# import plotly.express as px  # interactive charts
# import time

st.set_page_config(
    page_title="Real-Time Data Science Dashboard",
    page_icon="✅",
    layout="wide",
)

@st.experimental_singleton
def init_connection():
    return psycopg2.connect(**st.secrets["postgres"])

# def init_connection():
#     return psycopg2.connect(host='localhost',
#         database='smart_hand_sanitizer',
#         user='postgres',
#         password='rocky99')

conn = init_connection()

@st.experimental_memo
def get_data() -> pd.DataFrame:
    return pd.read_sql('SELECT * FROM sanitizer_records2', conn)

def get_data2() -> pd.DataFrame:
    return pd.read_sql('SELECT * FROM sanitizer_records3', conn)


SQL_Query = get_data()
SQL_Query2 = get_data2()

st.title("Real-Time / Live IoT Hand Santisier Dispenser")
# top-level filters
# hour_filter = st.selectbox("Select the Hour", pd.unique(SQL_Query["hours"]))
#
# # dataframe filter
# SQL_Query = SQL_Query[SQL_Query["hours"] == hour_filter]
#
# # create three columns
# kpi1, kpi2, kpi3 = st.columns(3)
#
# kpi1.metric(
#     label="Age ⏳",
#     value=round(avg_age),
#     delta=round(avg_age) - 10,
# )
#
# kpi2.metric(
#     label="Married Count 💍",
#     value=int(count_married),
#     delta=-10 + count_married,
# )
#
# kpi3.metric(
#     label="A/C Balance ＄",
#     value=f"$ {round(balance,2)} ",
#     delta=-round(balance / count_married) * 100,
# )



# st.write("My First Streamlit Web App")


#
# df = pd.DataFrame({"one": [1, 2, 3], "two": [4, 5, 6], "three": [7, 8, 9]})
# st.write(df)

# streamlit_app.py

# Initialize connection.

# def init_connection():
#     return psycopg2.connect(**st.secrets["postgres"])

# dataset_url = "https://raw.githubusercontent.com/Lexie88rus/bank-marketing-analysis/master/bank.csv"

# SQL_Query = pd.read_sql('SELECT id, date, hours FROM sanitizer_records1


    
st.write("Frequency of Smart Hand Sanitiser used")
df = pd.DataFrame(SQL_Query, columns=['id','date', 'hours'])
df2 = pd.DataFrame(SQL_Query2, columns=['id','date', 'hours'])

frequency = df['hours'].value_counts()
df_val_counts = pd.DataFrame(frequency) 
df_val_counts = df_val_counts.reset_index()
df_val_counts.columns = ['hour', 'frequency']

# frequency_df = df.value_counts().rename_axis('unique_values').to_frame('hours')
# print (df)
# frequency_df = pd.DataFrame()
# st.line_chart(df_val_counts, x = "hour", y="frequency")
# st.line_chart(df, x = "id", y="date")

# df = pd.DataFrame(SQL_Query, columns=['hours', 'date'])
# st.line_chart(df)
#
# df = pd.DataFrame(SQL_Query, columns=['hours'])
st.line_chart(df_val_counts, x = "hour", y="frequency")
# st.area_chart(df_val_counts, x = "hour", y="frequency")
# st.bar_chart(df_val_counts, x = "hour", y="frequency")
frequency_used = len(df['id'])
st.line_chart(df2, x = "date", y="id")

# # create two columns for charts
# fig_col1, fig_col2 = st.columns(2)
#
# with fig_col1:
#     st.markdown("### First Chart")
#     st.line_chart(df_val_counts, x = "hour", y="frequency")
#     # fig = px.density_heatmap(
#     #     data_frame=df, y="age_new", x="marital"
#     # )
#     # st.write(fig)

# st.line_chart(data=df,x='date', y='hours' )

# conn = psycopg2.connect(
#         host='localhost',
#         database='smart_hand_sanitizer',
#         user='postgres',
#         password='rocky99')
# st.markdown("### Detailed Data View")
# st.dataframe(df)
# Perform query.
# Uses st.experimental_memo to only rerun when the query changes or after 10 min.
@st.experimental_memo(ttl=60)
def run_query(query):
    with conn.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()


        # rows = run_query("SELECT * from sanitizer_records1;")

st.markdown("### Detailed Data View")
st.dataframe(SQL_Query2)


# creating a single-element container.


# # Print results.
# for row in rows:
#     st.write(f"{row[0]} has a :{row[1]}:")
    
 
    
    
    
    
    
    
