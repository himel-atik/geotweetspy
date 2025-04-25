import requests
import urllib.parse
import sys

def get_coordinates(address):
    """Convert address to GPS coordinates using Nominatim (OpenStreetMap)."""
    url = "https://nominatim.openstreetmap.org/search"
    params = {
        "q": address,
        "format": "json"
    }
    headers = {
        "User-Agent": "GeoSearchScript"
    }
    response = requests.get(url, params=params, headers=headers)
    data = response.json()
    if data:
        latitude = data[0]['lat']
        longitude = data[0]['lon']
        return float(latitude), float(longitude)
    else:
        raise ValueError("Address not found.")

def generate_twitter_geo_search_url(lat, lon, radius="1km", keyword=None):
    """Generate Twitter URL for geo-based tweet search."""
    base_url = "https://x.com/search?q="
    query = f"geocode:{lat},{lon},{radius}"
    if keyword:
        query += f" {keyword}"
    full_url = base_url + urllib.parse.quote(query) + "&f=live"
    return full_url

def display_usage():
    print("\n Twitter Geo Search Tool")
    print("You will be asked to input:")
    print("   1️⃣ Address (e.g., Times Square, New York)")
    print("   2️⃣ Radius (e.g., 1km or 2mi) [default: 1km]")
    print("   3️⃣ Keyword (e.g., fight) [optional]")
    print("-" * 50)

if __name__ == "__main__":
    display_usage()
    
    address = input("Enter address: ").strip()
    radius = input("Enter radius (e.g., 1km, 2mi) [default: 1km]: ").strip() or "1km"
    keyword = input("Enter keyword (optional): ").strip() or None

    try:
        lat, lon = get_coordinates(address)
        search_url = generate_twitter_geo_search_url(lat, lon, radius, keyword)
        print("\nTwitter Geo Search URL:")
        print(search_url)
    except ValueError as ve:
        print(f"\nError: {ve}")
    except Exception as e:
        print(f"\nUnexpected error: {e}")
