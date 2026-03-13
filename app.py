import streamlit as st
import polars as pl
import duckdb
import io
import pandas as pd

st.set_page_config(page_title=&quot;Palantir FDE Sim v0.1&quot;, page_icon=&quot;🛡️&quot;, layout=&quot;wide&quot;)

st.title(&quot;🛡️ Palantir FDE Simulator v0.1 MVP&quot;)

st.markdown(&quot;**FDE prep tool**: Dataset upload → ETL/deploy sim (DuckDB/Polars), case studies, interview mocks.&quot;)

tab1, tab2, tab3 = st.tabs([&quot;📊 Dataset ETL Sim&quot;, &quot;📚 Case Studies&quot;, &quot;🎤 Interview Mocks&quot;])

with tab1:
    st.header(&quot;Upload Dataset (CSV/JSON)&quot;)
    uploaded_file = st.file_uploader(&quot;Choose a CSV or JSON file&quot;, type=[&#x27;csv&#x27;, &#x27;json&#x27;, &#x27;jsonl&#x27;])

    if uploaded_file is not None:
        try:
            if uploaded_file.name.endswith(&#x27;.csv&#x27;):
                df = pl.read_csv(uploaded_file)
            elif uploaded_file.name.endswith((&#x27;.json&#x27;, &#x27;.jsonl&#x27;)):
                df = pl.read_ndjson(uploaded_file)
            else:
                df = pl.read_json(uploaded_file)
            st.success(f&quot;Loaded {df.shape[0]} rows x {df.shape[1]} cols&quot;)
        except Exception as e:
            st.error(f&quot;Error loading file: {e}&quot;)
            st.stop()

        col1, col2 = st.columns(2)
        with col1:
            st.subheader(&quot;Raw Data Preview&quot;)
            st.dataframe(df.head(500), use_container_width=True)
        with col2:
            st.subheader(&quot;Schema&quot;)
            st.json({&quot;columns&quot;: df.columns, &quot;dtypes&quot;: [str(t) for t in df.dtypes], &quot;shape&quot;: df.shape})

        # Summary
        st.subheader(&quot;ETL Insights (Polars describe)&quot;)
        summary = df.describe()
        st.dataframe(summary)

        # DuckDB Pipeline Sim
        st.subheader(&quot;Deploy Sim: DuckDB Query&quot;)
        con = duckdb.connect(&#x27;:memory:&#x27;)
        con.register(&quot;data&quot;, df.to_pandas())  # DuckDB with Polars via pandas
        default_query = &quot;SELECT COUNT(*) as row_count, AVG(*) FROM data LIMIT 10&quot;
        query = st.text_area(&quot;SQL Query&quot;, value=default_query, height=100)
        if st.button(&quot;🚀 Run ETL Query&quot;, type=&quot;primary&quot;):
            try:
                res = con.execute(query).fetchdf()
                st.dataframe(res)
                st.balloons()
            except Exception as e:
                st.error(f&quot;Query error: {e}&quot;)

        # Viz
        st.subheader(&quot;Auto-Viz&quot;)
        numeric_df = df.select([pl.col(c) for c in df.columns if df[c].dtype in [pl.Float64, pl.Int64, pl.UInt32]])
        if not numeric_df.is_empty():
            st.line_chart(numeric_df)

with tab2:
    st.header(&quot;FDE Case Studies&quot;)
    st.info(&quot;**Example Case**: Fraud detection pipeline. Upload transaction CSV, query anomalies with DuckDB, deploy sim.&quot;)
    # TODO more

with tab3:
    st.header(&quot;Interview Mock&quot;)
    st.info(&quot;**Mock Q1**: Design ETL for customer data platform. A: Use Polars for transform, DuckDB for query engine...&quot;)
    # TODO Gradio chat

st.sidebar.markdown(&quot;---&quot;)
st.sidebar.info(&quot;**Stack**: Streamlit UI, Polars/DuckDB ETL, Supabase (TBD), Vercel deploy.\\n**No API keys used.**&quot;)
st.sidebar.success(&quot;Ready for Palantir FDE prep!&quot;)