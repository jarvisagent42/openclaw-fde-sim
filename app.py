import streamlit as st
import polars as pl
import duckdb
import io
import pandas as pd

st.set_page_config(page_title="Palantir FDE Sim v0.1", page_icon="🛡️", layout="wide")

st.title("🛡️ Palantir FDE Simulator v0.1 MVP")

st.markdown("**FDE prep tool**: Dataset upload → ETL/deploy sim (DuckDB/Polars), case studies, interview mocks.")

tab1, tab2, tab3 = st.tabs(["📊 Dataset ETL Sim", "📚 Case Studies", "🎤 Interview Mocks"])

with tab1:
    st.header("Upload Dataset (CSV/JSON)")
    uploaded_file = st.file_uploader("Choose a CSV or JSON file", type=['csv', 'json', 'jsonl'])

    if uploaded_file is not None:
        try:
            if uploaded_file.name.endswith('.csv'):
                df = pl.read_csv(uploaded_file)
            elif uploaded_file.name.endswith(('.json', '.jsonl')):
                df = pl.read_ndjson(uploaded_file)
            else:
                df = pl.read_json(uploaded_file)
            st.success(f"Loaded {df.shape[0]} rows x {df.shape[1]} cols")
        except Exception as e:
            st.error(f"Error loading file: {e}")
            st.stop()

        col1, col2 = st.columns(2)
        with col1:
            st.subheader("Raw Data Preview")
            st.dataframe(df.head(500), use_container_width=True)
        with col2:
            st.subheader("Schema")
            st.json({"columns": df.columns, "dtypes": [str(t) for t in df.dtypes], "shape": df.shape})

        # Summary
        st.subheader("ETL Insights (Polars describe)")
        summary = df.describe()
        st.dataframe(summary)

        # DuckDB Pipeline Sim
        st.subheader("Deploy Sim: DuckDB Query")
        con = duckdb.connect(':memory:')
        con.register("data", df.to_pandas())  # DuckDB with Polars via pandas
        default_query = "SELECT COUNT(*) as row_count FROM data LIMIT 10"
        query = st.text_area("SQL Query", value=default_query, height=100)
        if st.button("🚀 Run ETL Query", type="primary"):
            try:
                res = con.execute(query).fetchdf()
                st.dataframe(res)
                st.balloons()
            except Exception as e:
                st.error(f"Query error: {e}")

        # Viz
        st.subheader("Auto-Viz")
        numeric_df = df.select([pl.col(c) for c in df.columns if df[c].dtype in [pl.Float64, pl.Int64, pl.UInt32]])
        if not numeric_df.is_empty():
            st.line_chart(numeric_df)

with tab2:
    st.header("FDE Case Studies")
    st.info("**Example Case**: Fraud detection pipeline. Upload transaction CSV, query anomalies with DuckDB, deploy sim.")
    # TODO more

with tab3:
    st.header("Interview Mock")
    st.info("**Mock Q1**: Design ETL for customer data platform. A: Use Polars for transform, DuckDB for query engine...")
    # TODO Gradio chat

st.sidebar.markdown("---")
st.sidebar.info("**Stack**: Streamlit UI, Polars/DuckDB ETL, Supabase (TBD), Vercel deploy.\n**No API keys used.**")
st.sidebar.success("Ready for Palantir FDE prep!")