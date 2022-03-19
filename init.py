import requests
import pandas as pd
from datetime import date, timedelta

# How many days back do you want the data from
days_ago = 5

# URL and Auth key for api verification 
APIKEY = 'asdjkyfejwgadkhsfgjh'
# Your electricity meter-point’s MPAN
MPAN = '1200060128968'
# Your electricity meter’s serial number
SR = '12L2368778'
url = 'https://api.octopus.energy/v1/electricity-meter-points/'+MPAN+'/meters/'+SR+'/consumption/'
# Returns a pandas DataFrame containing consumption data from days_ago ago
def get_days_ago(days_ago):

    # Which date of the data collected
    period_from = str(date.today() - timedelta(days=(days_ago+1)))
    period = '?period_from='+period_from+'T00:00Z&period_to='+period_from+'T23:30Z'

    # Request URL
    r = requests.get(url+period, auth=(APIKEY,''))

    # Convert to Pandas DataFrame from JSON
    output_dict = r.json()
    dataframe = pd.DataFrame.from_dict(output_dict['results'])

    return dataframe

# Colelct data from days_ago ago
data = get_days_ago(0)
for i in range(1, days_ago):
    data = data.append(get_days_ago(i))

# Dataframe reversed to add to CSV, newest at the bottom
data_reversed = data.iloc[::-1]

# Write to CSV
with open('Consumption.csv','w') as f:
    data_reversed.to_csv(f)




