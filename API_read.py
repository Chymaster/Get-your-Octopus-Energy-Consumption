import requests
import pandas as pd
from datetime import date, timedelta

# URL and Auth key for api verification 
APIKEY = 'asdjkyfejwgadkhsfgjh'
# Your electricity meter-point’s MPAN
MPAN = '1200060128968'
# Your electricity meter’s serial number
SR = '12L2368778'
url = 'https://api.octopus.energy/v1/electricity-meter-points/'+MPAN+'/meters/'+SR+'/consumption/'


# Set a time period
period_from = str(date.today() - timedelta(days=1))
period = '?period_from='+period_from+'T00:00Z&period_to='+period_from+'T23:30Z'

# Request URL
r = requests.get(url+period, auth=(APIKEY,''))

# Convert to Pandas DataFrame from JSON
output_dict = r.json()
dataframe = pd.DataFrame.from_dict(output_dict['results'])
# Dataframe reversed to add to CSV, newest at the bottom
dataframe_reversed = dataframe.iloc[::-1]

# Write to CSV
with open('Consumption.csv','a') as f:
    dataframe_reversed.to_csv(f, header = False)


