import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st

india = pd.read_csv("india.csv")
overall_india = list(india["State"].unique())
overall_india.insert(0, "Overall India")

cols = india.columns[5:]
st.success("Size represents primary Parameter")
st.warning("Color represents secondary Parameter")
st.sidebar.title("India Visualisation")
selected_state = st.sidebar.selectbox("Select a State", overall_india)
primary = st.sidebar.selectbox("Select primary Parameter", sorted(cols))
secondary = st.sidebar.selectbox("Select secondary Parameter", sorted(cols))
plot = st.sidebar.button("Plot Graph")

if plot:
    if selected_state == "Overall India":
        fig = px.scatter_map(
            india,
            lat="Latitude",
            lon="Longitude",
            zoom=3,
            map_style="carto-positron",
            size=primary,
            color=secondary,
            size_max=35,
            width=1200,
            height=700,
            hover_name="District",
        )
        st.plotly_chart(fig, use_container_width=True)
    else:
        states = india[india["State"] == selected_state]
        fig = px.scatter_map(
            states,
            lat="Latitude",
            lon="Longitude",
            zoom=3,
            map_style="carto-positron",
            size=primary,
            color=secondary,
            size_max=35,
            width=1200,
            height=700,
            hover_name="District",
        )
        st.plotly_chart(fig, use_container_width=True)
