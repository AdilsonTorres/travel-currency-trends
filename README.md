# 💱 Travel Currency Trends Tracker

**Real-time USD/BRL Exchange Rates & Market News for Travelers in Brazil**

![Streamlit Badge](https://img.shields.io/badge/Built%20with-Streamlit-FF4B4B?style=flat&logo=streamlit)
![Python Badge](https://img.shields.io/badge/Python-3.9+-3776ab?style=flat&logo=python)
![SerpApi Badge](https://img.shields.io/badge/Powered%20by-SerpApi-FF6B6B?style=flat)

## 🎯 Overview

**Travel Currency Trends Tracker** is a web application designed to help travelers, business professionals, and currency traders monitor real-time USD/BRL exchange rates and market trends. The app provides instant currency conversion, budget planning tools, and the latest financial news affecting exchange rates.

### 🚀 Live Demo

Hosted on Streamlit Cloud: [View Live Demo](https://travel-currency-trends.streamlit.app/)

## ✨ Features

- 💱 **Real-time Exchange Rates**: Current USD to BRL conversion rates
- 📈 **30-Day Trend Analysis**: Historical exchange rate charts and patterns
- 🧮 **Travel Budget Calculator**: Plan your trip budget with instant conversions
- 📰 **Market News**: Latest financial news affecting USD/BRL exchange rates
- 🔍 **Powered by SerpApi**: Real-time market data and news aggregation
- 📱 **Mobile-Friendly**: Responsive design works on all devices

## 📱 Pages

### 1. 🏠 Dashboard
- Current exchange rate display
- Quick currency conversions (1 USD, 1000 USD)
- 30-day trend visualization

### 2. 📈 Trends Analysis
- Market trend insights
- Latest financial news via SerpApi
- Currency market analysis

### 3. 🧮 Travel Calculator
- Convert USD amounts to BRL
- Budget breakdown by category:
  - 🏨 Accommodation
  - 🍽️ Food & Dining
  - 🎭 Activities & Entertainment

### 4. 📰 Market News
- Search market news
- Latest financial updates
- Currency market insights

### 5. ℹ️ About
- Project information
- Feature overview
- Technology details

## 🛠️ Technology Stack

- **Framework**: Streamlit (Python web framework)
- **APIs**: SerpApi (market news), ExchangeRate-API (exchange rates)
- **Language**: Python 3.9+
- **Data Processing**: Pandas
- **HTTP Client**: Requests

## 📋 Requirements

- Python 3.9 or higher
- SerpApi API Key (free tier available)
- Internet connection for real-time data

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/AdilsonTorres/travel-currency-trends.git
cd travel-currency-trends
```

### 2. Create Virtual Environment

```bash
# On macOS/Linux
python3 -m venv venv
source venv/bin/activate

# On Windows
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables

```bash
# Copy the example file
cp .env.example .env

# Edit .env and add your SerpApi key
# SERPAPI_KEY=your_key_here
```

### 5. Get Your SerpApi Key

1. Go to [SerpApi Sign Up](https://serpapi.com/users/sign_up)
2. Create a free account (250 free searches per month)
3. Get your API key at [Manage API Keys](https://serpapi.com/manage-api-key)
4. Add it to your `.env` file

### 6. Run the Application

```bash
streamlit run app.py
```

The app will open at `http://localhost:8501`

## 🚀 Deployment to Streamlit Cloud

### Steps:

1. **Push to GitHub** (already done)
   ```bash
   git push origin main
   ```

2. **Go to Streamlit Cloud**
   - Visit https://streamlit.io/cloud
   - Sign in with GitHub
   - Click "New app"

3. **Configure Deployment**
   - Repository: `AdilsonTorres/travel-currency-trends`
   - Branch: `main`
   - Main file path: `app.py`
   - Click "Deploy"

4. **Add Secrets**
   - In Streamlit Cloud dashboard, go to Settings
   - Add your SerpApi key as a secret:
     ```
     SERPAPI_KEY = "your_key_here"
     ```

5. **Access Your App**
   - Your app will be live at: `https://travel-currency-trends.streamlit.app/`

## 📊 Data Sources

- **Exchange Rates**: ExchangeRate-API
- **Market News**: SerpApi (Google News API)
- **Trend Data**: Real-time market data

## 🎓 How to Use

### For Travelers:
1. Enter your budget in USD on the Travel Calculator page
2. View the equivalent in BRL with current exchange rates
3. Plan budget breakdown by category
4. Check market news for currency trends

### For Researchers:
1. View 30-day exchange rate trends
2. Access latest financial news
3. Search for specific market topics
4. Analyze currency market patterns

## 📝 Project Structure

```
travel-currency-trends/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── .env.example          # Environment variables template
├── .gitignore            # Git ignore rules
└── README.md             # This file
```

## 🔐 Security Notes

- **Never commit `.env` file** with real API keys
- Always use `.env.example` as a template
- On Streamlit Cloud, use Secrets management
- Keep your SerpApi key private and confidential

## 🐛 Troubleshooting

### "API Key not found" error
- Check if `.env` file exists in the project root
- Ensure `SERPAPI_KEY=your_key` is correctly set
- On Streamlit Cloud, verify the secret is added

### "No news found" message
- Verify your SerpApi key is valid and has remaining searches
- Check internet connection
- Try a different search query

### Exchange rate not updating
- Check ExchangeRate-API status
- Verify internet connection
- Try refreshing the page

## 📈 Use Cases

1. **Travel Planning**: Budget your Brazil trip in real-time
2. **Business**: Monitor USD/BRL for international transactions
3. **Investment**: Track currency trends for forex trading
4. **Research**: Analyze market data and financial news
5. **Education**: Learn about currency markets and APIs

## 🎯 Target Audience

- 🇧🇷 Tourists planning trips to Brazil
- 💼 Business travelers
- 🏦 Currency traders and analysts
- 📊 Financial researchers
- 👨‍💻 Developers learning SerpApi integration

## 📚 API Documentation

- [SerpApi Documentation](https://serpapi.com/search-engine-apis)
- [SerpApi Python SDK](https://serpapi.com/integrations/python)
- [Streamlit Documentation](https://docs.streamlit.io/)

## 📄 License

This project is open-source and available under the MIT License.

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests
- Share ideas

## 👨‍💼 Author

**Adilson Torres**
- GitHub: [@AdilsonTorres](https://github.com/AdilsonTorres)

## 🎉 Raffle Challenge

Built for the **Anaconda Labs SerpApi Raffle Challenge**

---

## 📞 Support

For issues, questions, or suggestions:
1. Check the [GitHub Issues](https://github.com/AdilsonTorres/travel-currency-trends/issues)
2. Review the troubleshooting section above
3. Contact the developer

---

**Made with ❤️ using SerpApi and Streamlit**
