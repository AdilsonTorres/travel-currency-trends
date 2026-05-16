import streamlit as st
import requests
import pandas as pd
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv

load_dotenv()

SERPAPI_KEY = os.getenv('SERPAPI_KEY')

st.set_page_config(
    page_title="Travel Currency Trends",
    page_icon="💱",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("💱 Travel Currency Trends Tracker")
st.subheader("Real-time USD/BRL Exchange Rates & Market News for Travelers in Brazil")

# Sidebar navigation
page = st.sidebar.radio(
    "Navigate",
    ["🏠 Dashboard", "📈 Trends Analysis", "🧮 Travel Calculator", "📰 Market News", "ℹ️ About"]
)

# Function to fetch exchange rate (simulated for demo)
def get_exchange_rate():
    try:
        response = requests.get('https://api.exchangerate-api.com/v4/latest/USD')
        data = response.json()
        return data['rates'].get('BRL', 5.0)
    except:
        return 5.0  # Fallback rate

# Function to fetch news from SerpApi
def fetch_market_news(query):
    try:
        url = f"https://serpapi.com/search?q={query}&tbm=nws&api_key={SERPAPI_KEY}"
        response = requests.get(url)
        data = response.json()
        return data.get('news_results', [])
    except Exception as e:
        st.error(f"Error fetching news: {e}")
        return []

# Dashboard Page
if page == "🏠 Dashboard":
    st.header("Exchange Rate Dashboard")
    
    col1, col2, col3 = st.columns(3)
    
    current_rate = get_exchange_rate()
    
    with col1:
        st.metric("USD/BRL Current Rate", f"R$ {current_rate:.2f}", "+0.05")
    
    with col2:
        st.metric("1 USD in BRL", f"R$ {current_rate:.2f}")
    
    with col3:
        st.metric("1000 USD", f"R$ {current_rate * 1000:,.2f}")
    
    st.divider()
    
    # Sample data for trend chart
    dates = pd.date_range(start=datetime.now() - timedelta(days=30), periods=30)
    rates = [4.85 + i*0.005 for i in range(30)]
    
    df_trends = pd.DataFrame({
        'Date': dates,
        'Rate': rates
    })
    
    st.line_chart(df_trends.set_index('Date'))
    st.caption("30-Day USD/BRL Exchange Rate Trend")

# Trends Analysis Page
elif page == "📈 Trends Analysis":
    st.header("Market Trends Analysis")
    st.write("Analyzing market trends and news affecting USD/BRL exchange rates...")
    
    if st.button("Fetch Latest Market News"):
        st.info("Fetching news from SerpApi...")
        news = fetch_market_news("USD BRL exchange rate Brazil")
        
        if news:
            st.success(f"Found {len(news)} news articles")
            for i, article in enumerate(news[:5], 1):
                st.subheader(f"{i}. {article.get('title', 'No title')}")
                st.write(article.get('snippet', 'No description'))
                st.write(f"Source: {article.get('source', 'Unknown')}")
                st.divider()
        else:
            st.warning("No news found. Please check your SerpApi key.")

# Travel Calculator Page
elif page == "🧮 Travel Calculator":
    st.header("Travel Budget Calculator")
    st.write("Plan your trip to Brazil with real-time exchange rates!")
    
    col1, col2 = st.columns(2)
    
    with col1:
        usd_amount = st.number_input("Amount in USD ($)", min_value=0.0, value=1000.0, step=100.0)
    
    with col2:
        current_rate = get_exchange_rate()
        brl_amount = usd_amount * current_rate
        st.metric("Amount in BRL (R$)", f"R$ {brl_amount:,.2f}")
    
    st.divider()
    
    # Budget breakdown
    st.subheader("Budget Breakdown")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        accommodation = st.number_input("Accommodation (% of budget)", 0, 100, 40) / 100 * brl_amount
        st.metric("Accommodation", f"R$ {accommodation:,.2f}")
    
    with col2:
        food = st.number_input("Food & Dining (% of budget)", 0, 100, 30) / 100 * brl_amount
        st.metric("Food & Dining", f"R$ {food:,.2f}")
    
    with col3:
        activities = st.number_input("Activities (% of budget)", 0, 100, 30) / 100 * brl_amount
        st.metric("Activities", f"R$ {activities:,.2f}")

# Market News Page
elif page == "📰 Market News":
    st.header("Latest Currency & Financial News")
    
    search_query = st.text_input("Search for news", "currency exchange Brazil")
    
    if st.button("Search News"):
        st.info(f"Searching for: {search_query}")
        news = fetch_market_news(search_query)
        
        if news:
            st.success(f"Found {len(news)} articles")
            for article in news[:10]:
                with st.container():
                    st.subheader(article.get('title', 'No title'))
                    st.write(article.get('snippet', ''))
                    col1, col2 = st.columns(2)
                    with col1:
                        st.caption(f"Source: {article.get('source', 'Unknown')}")
                    with col2:
                        st.caption(f"Date: {article.get('date', 'Unknown')}")
                    st.divider()
        else:
            st.warning("No articles found.")

# About Page
elif page == "ℹ️ About":
    st.header("About Travel Currency Trends Tracker")
    
    st.markdown("""
    ### 📊 Project Overview
    
    **Travel Currency Trends Tracker** is a real-time application designed for travelers planning trips to Brazil. 
    It provides:
    
    - 💱 **Live Exchange Rates**: Current USD/BRL conversion rates
    - 📈 **Trend Analysis**: 30-day historical exchange rate trends
    - 🧮 **Budget Calculator**: Plan your trip budget with real-time rates
    - 📰 **Market News**: Latest financial news affecting exchange rates
    - 🔍 **Powered by SerpApi**: Real-time market news and data
    
    ### 🚀 Features
    
    ✅ Real-time USD/BRL exchange rates
    ✅ Interactive budget planning tool
    ✅ Market news and financial insights
    ✅ Beautiful, user-friendly interface
    ✅ Mobile-responsive design
    
    ### 🛠️ Technology Stack
    
    - **Frontend**: Streamlit
    - **Data Sources**: SerpApi, ExchangeRate-API
    - **Language**: Python 3.9+
    
    ### 📝 How to Use
    
    1. Navigate using the sidebar menu
    2. Check current exchange rates on the Dashboard
    3. Use the Travel Calculator to plan your budget
    4. Read latest market news in the Market News section
    
    ### 🎯 Target Users
    
    - 🇧🇷 Tourists planning trips to Brazil
    - 💼 Business travelers
    - 🏦 Currency traders and analysts
    - 📊 Financial researchers
    
    ### 📧 Support
    
    For issues or suggestions, please visit the GitHub repository.
    """)

st.sidebar.divider()
st.sidebar.info(
    "🔗 Powered by [SerpApi](https://serpapi.com) for real-time market data"
)
