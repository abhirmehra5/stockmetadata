from ib_insync import *
import pandas as pd
data = pd.read_csv("tickers_Abhir.csv")
stocks = data["Ticker"]
df2=pd.DataFrame(columns = ["contract","industry","longName","marketName","secIdList"])
df3=pd.DataFrame(columns = ["contract","industry","longName","marketName","secIdList"])

ib = IB()
ib.connect('127.0.0.1', 7496, clientId=99)
for i in stocks:
    contract = Stock(i)
    try:
        bars = ib.reqContractDetails(contract)
        df = pd.DataFrame(bars)
        cleandata = df[["contract","industry","longName", "marketName", "secIdList"]]
        cleandata = cleandata.explode('secIdList')
        cleandata = cleandata.drop_duplicates(subset=["secIdList"])
        df2 = pd.concat([df2, cleandata])
    except:
        df2 =pd.concat([df2,df3])


df2.to_csv('ibdata_unclean_Abhir.csv')

