# March 27 2021
# NASADailyBackground Project
# Calls NASA APOD API Downloads the HD Daily image, saves to home directory using given title

# Call the API
import requests
import json
import config

response = requests.get('https://api.nasa.gov/planetary/apod?api_key={}'.format(config.api_key))

json_object = json.loads(response.text)

hd_image = requests.get(json_object["hdurl"])

title = json_object["title"]

# Download APOD to Folder

open_picture_location = f"{config.home_dir}{title}.png"

with open(open_picture_location,'wb') as f:
    f.write(hd_image.content)
