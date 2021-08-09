#!/usr/bin/env python3
"""
Scrapes http://troutfitters.com for current fly fishing conditions.
Creates a test file with:
    river conditions with river name
    date
    intro
    pattern suggestions

File will later be uploaded to S3 where a lambda function will convert text file to a mp3 using AWS Polly.
After which be used in an Alexa app for Southwestern Fly Fishing Conditions. 

Future turn this script into a Lambda function. Maybe include more rivers, weather conditions, and river
flow conditions. 
"""

from requests import get
from bs4 import BeautifulSoup
from datetime import date

import requests

sw_rivers = {
"Gallatin":"https://troutfitters.com/index.php/fishing-reports/river/gallatin-river",
"Lower Madison":"https://troutfitters.com/index.php/fishing-reports/river/lower-madison-river",
"Upper Madison":"https://troutfitters.com/index.php/fishing-reports/river/upper-madison-river",
"Yellowstone":"https://troutfitters.com/index.php/fishing-reports/river/yellowstone-river",
"Spring Creek":"https://troutfitters.com/index.php/fishing-reports/river/spring-creeks",
"Big Hole":"https://troutfitters.com/index.php/fishing-reports/river/big-hole",
"Boulder":"https://troutfitters.com/index.php/fishing-reports/river/boulder-river",
"Bighorn":"https://troutfitters.com/index.php/fishing-reports/river/big-horn-river",
"Missouri":"https://troutfitters.com/index.php/fishing-reports/river/missouri-river",
"Yellowstone Park Waters":"https://troutfitters.com/index.php/fishing-reports/river/yellowstone-park-waters",
"Other Waters":"https://troutfitters.com/index.php/fishing-reports/river/other-waters"
}

for key, value in sw_rivers.items():
    # Adds rivers and address for lookup
    river = key 
    address = value

    # with open("../text/%s.txt" % river, 'w') as f:
    f = open("../text/%s.txt" % river, 'w')

    page = requests.get(address)

    soup = BeautifulSoup(page.text, 'html.parser')

    # Date
    today = date.today()
    f.write(today.strftime("%B %d, %Y"))
    f.write('\n\n')

    # Fishing Conditions
    fishing_conditions = (f"Fishing Coditions for the {river}.")
    f.write(fishing_conditions)
    f.write('\n\n')

    # Intro
    intro = soup.find_all('p')[0].get_text()
    f.write(intro)
    f.write('\n\n')

    # Fly Pattern Suggestions: Label
    suggestions = "Fly Pattern Suggestions"
    f.write(suggestions)
    f.write('\n\n')    

    # Patterns: Dries, Nymphs, and Streamers
    patterns = soup.find_all('p')[2].get_text()
    f.write(patterns)

    f.close
    


