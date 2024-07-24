# hospitals.py
import requests
from location import get_location

def get_nearby_hospitals():
    """Get a list of nearby hospitals using the Overpass API."""
    latitude, longitude = get_location()  # Get coordinates from location.py

    overpass_url = "http://overpass-api.de/api/interpreter"
    overpass_query = f"""
    [out:json];
    (
      node["amenity"="hospital"](around:5000, {latitude}, {longitude});
      way["amenity"="hospital"](around:5000, {latitude}, {longitude});
      relation["amenity"="hospital"](around:5000, {latitude}, {longitude});
    );
    out body;
    """
    response = requests.get(overpass_url, params={'data': overpass_query})

    print("Status Code:", response.status_code)
    print("Response Text:", response.text)

    try:
        data = response.json()
        hospitals = data.get('elements', [])
        return hospitals
    except requests.exceptions.JSONDecodeError:
        print("Error decoding JSON from response.")
        return []

if __name__ == "__main__":
    hospitals = get_nearby_hospitals()
    if hospitals:
        print("Nearby Hospitals:")
        for hospital in hospitals:
            if 'tags' in hospital:
                name = hospital['tags'].get('name', 'No Name')
                latitude = hospital.get('lat', 'No Latitude')
                longitude = hospital.get('lon', 'No Longitude')
                print(f"Name: {name}")
                print(f"Latitude: {latitude}, Longitude: {longitude}")
                print()
    else:
        print("No nearby hospitals found.")
