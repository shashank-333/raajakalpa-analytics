import os
import streamlit as st
import pandas as pd
import plotly.express as px
from dotenv import load_dotenv
from langchain_community.document_loaders import TextLoader
from langchain_classic.indexes import VectorstoreIndexCreator
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings

# 1. Load Gemini API Key
load_dotenv()

# Set up browser page configuration (Wide mode for enterprise look)
st.set_page_config(page_title="Raajakalpa Financials", layout="wide", page_icon="🏗️")

# Custom Minimalist UI Injection
st.markdown("""
    <style>
    .block-container { padding-top: 2rem; padding-bottom: 2rem; }
    h1, h2, h3 { font-weight: 400; }
    </style>
""", unsafe_allow_html=True)

# 2. Hardcoded structured data for metrics and charting
@st.cache_data
def load_structured_data():
    data = {
        "Category": [
            "Structure", "Woodwork", "Plastering", "Flooring", 
            "Painting", "Plumbing", "Compound", "Operations", 
            "Electrical", "Fabrication", "Openings", "Kitchen App",
            "Unaccounted Variance"
        ],
        "Total Spent (INR)": [
            1114424, 455000, 280500, 260000, 
            227550, 157500, 149100, 134000, 
            122930, 115500, 90917, 31150,
            32300 
        ]
    }
    df = pd.DataFrame(data).sort_values(by="Total Spent (INR)", ascending=False)
    # Calculate percentage of total for professional insights
    total = df["Total Spent (INR)"].sum()
    df["% of Total"] = (df["Total Spent (INR)"] / total * 100).round(1)
    return df

df = load_structured_data()
total_budget = df["Total Spent (INR)"].sum()

# Minimalist color palette (Sage, Concrete, Muted Earth)
custom_colors = ['#7A8B7A', '#9BAA9B', '#B4BCB4', '#D0D6D0', '#8A9286', '#A1A89D']

# 3. AI Backend Engine (RAG)
@st.cache_resource
def load_ai_engine():
    loader = TextLoader('raajakalpa_budget.txt')
    embeddings = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001")
    return VectorstoreIndexCreator(embedding=embeddings).from_loaders([loader])

index = load_ai_engine()
llm = ChatGoogleGenerativeAI(model="gemini-3.5-flash")

# --- ENTERPRISE DASHBOARD LAYOUT ---

st.title("🏗️ Raajakalpa Financial Intelligence")
st.markdown("Comprehensive audit and tracking interface for project expenditures.")

# Top Tier Feature 1: Tabbed Navigation
tab1, tab2, tab3 = st.tabs(["📊 Executive Overview", "📁 Deep Dive Data", "💬 AI Financial Analyst"])

with tab1:
    # Top Tier Feature 2: Contextual KPI Cards
    st.subheader("Key Performance Indicators")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Project Expenditure", f"₹{total_budget:,.0f}")
    col2.metric("Highest Outlay Category", df.iloc[0]["Category"])
    col3.metric("Top Category Cost", f"₹{df.iloc[0]['Total Spent (INR)']:,.0f}")
    col4.metric("Audit Variance", f"₹{df[df['Category'] == 'Unaccounted Variance']['Total Spent (INR)'].values[0]:,.0f}")
    
    st.markdown("---")
    
    # Top Tier Feature 3: Advanced Interactive Visualizations
    col_chart1, col_chart2 = st.columns(2)
    
    with col_chart1:
        st.write("**Expenditure Hierarchy (Treemap)**")
        fig_tree = px.treemap(
            df, path=['Category'], values='Total Spent (INR)',
            color='Total Spent (INR)', color_continuous_scale="Greens"
        )
        fig_tree.update_layout(margin=dict(t=10, l=10, r=10, b=10))
        st.plotly_chart(fig_tree, use_container_width=True)

    with col_chart2:
        st.write("**Budget Distribution (Donut)**")
        fig_donut = px.pie(
            df, names='Category', values='Total Spent (INR)', hole=0.4,
            color_discrete_sequence=custom_colors
        )
        fig_donut.update_traces(textposition='inside', textinfo='percent+label')
        fig_donut.update_layout(margin=dict(t=10, l=10, r=10, b=10), showlegend=False)
        st.plotly_chart(fig_donut, use_container_width=True)

with tab2:
    st.subheader("Audited Line Items & Exports")
    
    # Top Tier Feature 4: Interactive Filtering & Data Export
    selected_cats = st.multiselect("Filter by Department:", options=df["Category"], default=list(df["Category"]))
    filtered_df = df[df["Category"].isin(selected_cats)]
    
    st.dataframe(
        filtered_df.style.format({"Total Spent (INR)": "₹{:,.0f}", "% of Total": "{:.1f}%"}), 
        use_container_width=True, 
        hide_index=True
    )
    
    # Export capability
    csv = filtered_df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Download Filtered Report as CSV",
        data=csv,
        file_name='raajakalpa_financials.csv',
        mime='text/csv',
    )

with tab3:
    st.subheader("RAG-Powered AI Consultant")
    st.info("Querying the foundational text logs. Ask about specific material costs, contractor wages, or line-item breakdowns.")
    
    user_question = st.text_input("Enter your query:")
    
    if user_question:
        with st.spinner("Analyzing ledger data..."):
            answer = index.query(user_question, llm=llm)
            st.success(answer)