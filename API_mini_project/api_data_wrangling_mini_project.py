# Import QUANDL_API_KEY from the .env file
from dotenv import load_dotenv
load_dotenv(verbose=True)

import os
API_KEY = os.getenv("QUANDL_API_KEY")

#print(type(API_KEY))
#print(API_KEY)

# First, import the relevant modules
import requests

#Collect Data for 2017
# set API call parameters
database_code = 'FSE' # Frankfurt Stock Exchange Database
dataset_code = 'AFX_X' #Ticker symbol for Carl Zeiss Meditec
start_date = '2017-01-01'
end_date = '2017-12-31'

url = 'https://www.quandl.com/api/v3/datasets/'+database_code+'/'+dataset_code+'/data.json'

payload = {'api_key': API_KEY, 'start_date': start_date, 'end_date': end_date}

r = requests.get(url, params=payload)

# save the json response data to a dict
d = r.json()

lst = d['dataset_data']['data'] #extract the List of lists Data from the dict for processing
#print(lst)


#extract relevant variables opening, high, low, closing, trading volume respectively at colums of indices 1,2,3,4,6 of the list
opening = []
closing = []
high = []
low = []
trading_vol = []

for l in lst :
    #print(l[1])
    opening.append(l[1])
    high.append(l[2])
    low.append(l[3])
    closing.append(l[4])
    trading_vol.append(l[6])

# 3. Calculate what the highest and lowest opening prices were for the stock in this period.

# This operation is redundant since I realized I was looking at the wrong timeframe which had None values
# I'll keep it so if I need to change the timeframe I can still use this code.

# We observe that opening has some missing values while closing doesn't
#print(opening)
#print(closing)
# How do we handle missing values?
# We will replace the missing values in opening with the closing value for the same day.
clean_opening = []
for idx, val in enumerate(opening):
    if val is None:
        clean_opening.append(closing[idx])
    else :
        clean_opening.append(val)
# Verify that this worked correctly
#print(clean_opening)
#print(closing)

highest_opening = max(clean_opening)
lowest_opening = min(clean_opening)
print('The higest opening price for ', dataset_code, ' in 2017 is: ', highest_opening)
print('The lowest opening price for ', dataset_code, ' in 2017 is: ', lowest_opening)

# 4. What was the largest change in any one day (based on High and Low price)?
hi_lo_change = []
for idx, val in enumerate(high):
    hi_lo_change.append(val-low[idx])

max_hi_lo_change = max(hi_lo_change)
print('The largest daily change in any one day (based on High and Low price) for ', dataset_code, ' in 2017 is: ', round(max_hi_lo_change,2))

# 5. What was the largest change between any two days (based on Closing Price)?

# this does the WRONG thing. It computes the change with respect to the day before. The question asks largest change between any two days...
# day_daybefore_change = []
# for idx, val in enumerate(closing):
#     if idx == 0 :
#         day_daybefore_change.append(0)
#     else :
#         day_daybefore_change.append(val-closing[idx-1])

# max_day_daybefore_change = max(day_daybefore_change)
# print('The largest change between any two days (based on Closing Price) for ', dataset_code, ' in 2017 is: ', round(max_day_daybefore_change,2))

# solution is trivial max closing - min closing
print('The largest change between any two days (based on Closing Price) for ', dataset_code, ' in 2017 is: ', round(max(closing)-min(closing),2))


# 6. What was the average daily trading volume during this year?

# This operation is redundant since I realized I was looking at the wrong timeframe which had None values
# I'll keep it so if I need to change the timeframe I can still use this code.
#Trading vol has some None values too. We will replace them with zero.
#print(trading_vol)
clean_trading_vol = []
for idx, val in enumerate(trading_vol):
    if val is None:
        clean_trading_vol.append(0)
    else :
        clean_trading_vol.append(val)

avg_daily_trade_vol = sum(clean_trading_vol) / len(clean_trading_vol)
print('The average daily trading volume for ', dataset_code, ' in 2017 is: ', round(avg_daily_trade_vol,2))

# 7. What was the median trading volume during this year. (Note: you may need to implement your own function for calculating the median.)

import statistics

median_daily_trade_vol = statistics.median(clean_trading_vol)
print('The median trading volume for ', dataset_code, ' in 2017 is: ', round(median_daily_trade_vol,2))
