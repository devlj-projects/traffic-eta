import requests
import datetime
from dotenv import load_dotenv
import os
import pytz

timezone = pytz.timezone("Australia/Victoria")
current_dt = datetime.datetime.now(timezone)
formatted_dt = current_dt.strftime("%A, %B %d, %Y at %I:%M %p")

load_dotenv()
API_KEY = os.getenv("ORS_API_KEY")

#hardcoded origin/starting point and destination for now
ORIGIN_LAT = float(os.getenv("ORIGIN_LAT"))
ORIGIN_LONG = float(os.getenv("ORIGIN_LONG"))
DEST_LAT = float(os.getenv("DEST_LAT"))
DEST_LONG = float(os.getenv("DEST_LONG"))


#main function. Uses coords from .env, uses requests module to make http request to ORS API. API responds with JSON, in which has a 'duration' entry. 

def get_travel_time(ORIGIN_LAT, ORIGIN_LONG, DEST_LAT, DEST_LONG):
    headers = {'Accept': 'application/json, application/geo+json, application/gpx+xml, img/png; charset=utf-8',}
    call = requests.get(      
        f'https://api.heigit.org/openrouteservice/v2/directions/driving-car?api_key={API_KEY}'
        f'&start={ORIGIN_LONG},{ORIGIN_LAT}'
        f'&end={DEST_LONG},{DEST_LAT}',
        headers=headers)
    
    duration_data = call.json()
    duration = duration_data["features"][0]["properties"]["summary"]["duration"]
    return duration
   
if __name__ == "__main__":
    result = (get_travel_time(ORIGIN_LAT, ORIGIN_LONG, DEST_LAT, DEST_LONG)) / 60
    formatted_result = round(result, 2)

    print(f"\n>>> Travel time to Holmesglen Chadstone for {formatted_dt}: {formatted_result} minutes\n")


