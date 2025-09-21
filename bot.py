# bot.py (minimal test)
import requests, os
from datetime import datetime

API_KEY = os.getenv("TD_API_KEY")
BASE = "https://api.twelvedata.com/time_series"
SYMS = ["USD/JPY","GBP/JPY","XAU/USD"]

def test_fetch(sym):
    r = requests.get(BASE, params={"symbol":sym, "interval":"5min","outputsize":1, "apikey":API_KEY}, timeout=20).json()
    return r

if __name__ == "__main__":
    for s in SYMS:
        try:
            data = test_fetch(s)
            print(datetime.now(), s, "=>", data.get("values", [{"close":"err"}])[0]["close"])
        except Exception as e:
            print("ERR", s, e)
