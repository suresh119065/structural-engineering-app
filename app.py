import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Structural Engineering Data Analysis", layout="wide")
st.title("🏗️ Structural Engineering Data Analysis")

uploaded_file = st.file_uploader("Upload your Excel file", type=["xlsx"])

if uploaded_file:
    try:
        df = pd.read_excel(uploaded_file)
        st.subheader("Data Preview:")
        st.dataframe(df)

        # Example: Plotting first two numerical columns
        numeric_cols = df.select_dtypes(include='number').columns
        if len(numeric_cols) >= 2:
            x_col, y_col = numeric_cols[:2]
            fig = px.line(df, x=x_col, y=y_col, title=f"{y_col} vs {x_col}")
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.warning("Not enough numeric data to plot a chart.")
    except Exception as e:
        st.error(f"Error processing file: {e}")
