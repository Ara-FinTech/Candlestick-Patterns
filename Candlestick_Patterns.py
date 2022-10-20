import talib
import yfinance as yf

sym_data = yf.download("SPY",start = "2022-01-01", end= "2022-09-30")

#print(sym_data)

patt=talib.CDLENGULFING(sym_data['Open'],sym_data['High'],sym_data['Low'],sym_data['Close'])

print(patt[patt != 0])
