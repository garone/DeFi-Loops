# DeFi-Loops Calculator - Live Price Integration

✅ **Live price fetching from CoinGecko API has been added!**

## 🚀 How to Use

### Option 1: Run with Python Server (Recommended)
This avoids CORS issues and enables live price fetching.

```bash
# In the directory with index.html:
python server.py

# Or manually:
python -m http.server 8000
```

Then open: **http://localhost:8000**

### Option 2: Deploy Online
Deploy to any hosting service to enable live prices:

**Netlify Drop (Easiest):**
- Visit https://app.netlify.com/drop
- Drag and drop `index.html`
- Done! Live prices will work

**GitHub Pages:**
- Push to your GitHub repo
- Enable GitHub Pages in repo settings
- Your calculator will be live with working API calls

**Vercel/Netlify CLI:**
```bash
netlify deploy --dir=. --prod
```

### Option 3: Open Directly (Limited)
If you open `index.html` directly in your browser (double-click), the app uses a CORS proxy for API calls. This may be slower or occasionally fail.

## 🔄 Live Price Features

- **Fetch Live Prices button** - Gets current BTC/ETH prices from CoinGecko
- **Automatic updates** - Updates all token prices (cbBTC, cbETH, wstETH)
- **24h Price Changes** - Shows daily % changes for tracking
- **Auto-recalculation** - Refreshes your leverage strategy with new prices
- **Status updates** - Real-time feedback with timestamps

## 📊 Token Price Sources

- **cbBTC** → Bitcoin price
- **cbETH** → Ethereum price  
- **wstETH** → Ethereum price × 1.15 (staking premium)

## 🐛 Troubleshooting

**"Failed to fetch" error?**
→ Run with a local server (see Option 1)

**CORS issues?**
→ Don't open directly from file system, use a server

**API rate limits?**
→ CoinGecko free tier allows ~50 calls/min

## 🎯 Next Steps

Ready to add more features? Ideas:
- Save/load strategies to localStorage
- More tokens (WBTC, stETH, etc.)
- Export to PDF/CSV
- Dark mode toggle
- Historical price charts
- Gas cost calculator

---

**Questions?** The calculator is fully functional offline except for live price fetching, which requires internet + proper hosting.
