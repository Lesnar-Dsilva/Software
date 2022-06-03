import requests
key = "";#API Key
#"https://" REQUIRED
url = "https://www.google.com";
api = f"https://cutt.ly/api/api.php?key={key}&short={url}";
data = requests.get(api).json()["url"];
print("Shortened URL:",data["shortLink"]);
