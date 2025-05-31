import requests
from bs4 import BeautifulSoup, Comment

# Step 1: Fetch the HTML
url = "https://fbref.com/en/players/27d0a506/Pedro-Porro"
headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

# Step 2: Extract HTML comments (FBref hides tables in comments)
comments = soup.find_all(string=lambda text: isinstance(text, Comment))

# Step 3: Search for the relevant table (usually "stats_" prefix)
for comment in comments:
    if 'table' in comment:
        comment_soup = BeautifulSoup(comment, 'html.parser')
        table = comment_soup.find('table', {'id': 'stats_adv_standard'})  # or another table like 'stats_defense', etc.
        if table:
            rows = table.find_all('tr')
            for row in rows:
                stat_name = row.find('th', {'data-stat': 'stat'}).text.strip() if row.find('th', {'data-stat': 'stat'}) else None
                percentile_td = row.find('td', {'data-stat': 'percentile'})
                percentile = percentile_td.find('div').text.strip() if percentile_td else None

                if stat_name and percentile:
                    print(f"{stat_name}: {percentile}")
