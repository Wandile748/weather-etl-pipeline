import requests
import pandas as pd
from datetime import datetime
import os

def fetch_weather():
    url = "https://api.open-meteo.com/v1/forecast?latitude=-29.8579&longitude=31.0292&current=temperature_2m,relative_humidity_2m,weather_code,wind_speed_10m&timezone=Africa/Johannesburg"
    r = requests.get(url)
    data = r.json()
    print(data)
    current = data["current"]
    current["time"] = datetime.now().isoformat()
    current["city"] = "Durban"
    return current

weather = fetch_weather()
df = pd.DataFrame([weather])
os.makedirs("data", exist_ok=True)
df.to_csv(path, mode='a', header=not os.path.exists(path), index=False)
print(f"SAVED: {weather}")