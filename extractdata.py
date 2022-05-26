import pandas as pd

byCountry='https://docs.google.com/spreadsheets/d/1bXLjWwcF8Mlj5v06GFpdCvBMl3i1hUuCnXeMdlI9W_Q/edit#gid=0'
byDate='https://docs.google.com/spreadsheets/d/1bXLjWwcF8Mlj5v06GFpdCvBMl3i1hUuCnXeMdlI9W_Q/edit#gid=1472400329'

def cleanURL(url):
	return url.replace('/edit#gid=', '/export?format=csv&gid=')

urls = [(cleanURL(byCountry)), (cleanURL(byDate))]


rawdata = []
for url in urls:
    data = pd.read_csv(url)
    rawdata.append(data)
    # print(data.to_json())

rawdata[0].to_csv('UKR_emergency_byCountry.csv', index=False)
rawdata[1].to_csv('UKR_emergency_byDate.csv', index=False)
