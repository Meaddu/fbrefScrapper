import requests
from bs4 import BeautifulSoup

# Define the target URL for the player's FBref page
url = "https://fbref.com/en/players/27d0a506/Pedro-Porro"
headers = {"User-Agent": "Mozilla/5.0"}

# Send GET request to the page
response = requests.get(url, headers=headers, verify=False)
soup = BeautifulSoup(response.text, 'html.parser')

# Attempt to locate the advanced stat table by its known ID
table = soup.find('table', {'id': 'scout_summary_FB'})

# Verify that the table was found
if not table:
    print("Table 'scout_summary_FB' not found.")
else:
    print("Pedro Porro - Fullback Percentile Stats")
    print("----------------------------------------")

    rows = table.find_all('tr')
    stat_count = 0

    for row in rows:
        # Extract the statistic name (found in <th>) and percentile (found in <td data-stat="percentile">)
        stat_th = row.find('th')
        percentile_td = row.find('td', {'data-stat': 'percentile'})

        if stat_th and percentile_td:
            stat_name = stat_th.text.strip()
            percentile_div = percentile_td.find('div')
            percentile = percentile_div.text.strip() if percentile_div else None

            if stat_name and percentile:
                print(f"{stat_name}: {percentile}")
                stat_count += 1

    print("----------------------------------------")
    print(f"Total statistics extracted: {stat_count}")
