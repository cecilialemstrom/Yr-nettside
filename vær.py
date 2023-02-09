import requests

def naa(lengdegrad, breddegrad):
    url = f"https://api.met.no/weatherapi/locationforecast/2.0/complete?lat={lengdegrad}&lon={breddegrad}"
    res = requests.get(url, headers = { 'User-Agent': 'Cecilia' })
    data = res.json()

    print(data["properties"]["timeseries"][0]["data"]["next_1_hours"]["summary"])

def varsel(lengdegrad, breddegrad, timer):
    url = f"https://api.met.no/weatherapi/locationforecast/2.0/complete?lat={lengdegrad}&lon={breddegrad}"
    res = requests.get(url, headers = { 'User-Agent': 'Cecilia' })
    data = res.json()

    print(data["properties"]["timeseries"][timer]["data"]["next_1_hours"]["summary"]["symbol_code"])

naa(58.89, 10.52)

varsel(58.89, 10.52, 5)