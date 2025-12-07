YouTube Share of Voice (SoV) Analysis – Atomberg Fans

Project Description  
A Python script that fetches YouTube search results for a given query (“smart fan”), detects mentions of Atomberg or related keywords, and computes the Share of Voice (SoV) — the percentage of videos referencing Atomberg in the search results.

Features  
- Searches YouTube for a user‑defined keyword (“smart fan”) using the YouTube Data API v3.  
- Checks video titles and descriptions for Atomberg‑related keywords (like “atomberg”, “renesa”, “efficio”, etc.).  
- Outputs a list of videos — each with title, channel name, and whether it mentions Atomberg.  
- Calculates and displays total Atomberg mentions and SoV (in %).

Prerequisites  
- Python 3.10+ (recommended to upgrade to 3.11 or newer)  
- A valid YouTube Data API v3 key  
- "google-api-python-client" library installed  

Install dependencies with:  
"pip install google-api-python-client"
