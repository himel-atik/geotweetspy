# 🗺 Twitter Geo Search Tool

This tool allows you to convert any physical address into GPS coordinates and generate a real-time Twitter search URL to find tweets posted from nearby that location — optionally filtered by keyword and radius.

> Built with Python using OpenStreetMap’s Nominatim API.

---

## Features

- Convert any **address** to **latitude & longitude**
- Generate **Twitter search URLs** using geocode
- Optionally filter tweets by **keyword**
- Supports **custom radius** in `km` or `mi`
- Lightweight and fast (CLI tool)

---

## Requirements

- Python 3.x
- `requests` module

Install it using:
```bash
pip install requests
```

---

## 🛠 How to Use

### 🖥 Run the Tool
```bash
python3 geotweetspy.py
```

### You will be prompted to enter:
- Address (e.g., *New York City* or *1600 Amphitheatre Parkway, Mountain View, CA*)
- Radius (e.g., `1km`, `2mi`)
- Optional keyword (e.g., `fire`, `protest`, `accident`)

###  Output
It will print a direct **Twitter search URL** like this:

```
🔍 Twitter Geo Search URL:
https://x.com/search?q=geocode:40.7128,-74.0060,1km%20fire&f=live
```

Open the link to view real-time tweets from that location.

---

## 🧠 Example Use Cases

- **OSINT investigations**
- **Crime tracking**
- **Missing person activity**
- **Local trend analysis**
- **Disaster monitoring**

---

##  Notes

- Results depend on tweets being **location-enabled** (few users share precise location).
- This tool uses the free [OpenStreetMap Nominatim API](https://nominatim.org/), so please avoid abusing it.

---

## 📄 License

This project is open-source and free to use under the [MIT License](LICENSE).

---

## ✨ Credits

Made ❤️ by [MD Himel Atik]  
Follow on Twitter/X: [@mdhimelatik](https://x.com/mdhimelatik)
