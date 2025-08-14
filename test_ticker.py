import yfinance as yf

# Test with a company name
ticker = yf.Ticker("Microsoft")

# Check if we can get info
try:
    print("--- Testing with 'Microsoft' ---")
    print(ticker.info['symbol'])
except Exception as e:
    print(f"Error for 'Microsoft': {e}")

# Test with another company name
ticker = yf.Ticker("Google")

# Check if we can get info
try:
    print("\n--- Testing with 'Google' ---")
    print(ticker.info['symbol'])
except Exception as e:
    print(f"Error for 'Google': {e}")

# Test with a known ticker
ticker = yf.Ticker("GOOG")

# Check if we can get info
try:
    print("\n--- Testing with 'GOOG' ---")
    print(ticker.info['symbol'])
except Exception as e:
    print(f"Error for 'GOOG': {e}")
