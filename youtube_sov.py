from googleapiclient.discovery import build

api_key = "AIzaSyD2tSNeDtWW5bR1arF_pA4_C5ztaiCwiSU"   # paste your key here

youtube = build("youtube", "v3", developerKey=api_key)

request = youtube.search().list(
    q="smart fan",
    part="snippet",
    maxResults=10
)
response = request.execute()

print(response)
