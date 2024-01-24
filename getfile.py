#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 16:04:17 2024

@author: masoud

gets a URL and a file format and streams all the files their format match

"""

import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import urljoin

file_format = '.zip'
url = 'URL HERE'  # Replace with the base URL of the website

# Send a request to the URL
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find all MP3 files
for link in soup.find_all('a'):
    file_link = link.get('href')
    if file_link and file_link.endswith(file_format):
        full_link = urljoin(url, file_link)  # Construct the full URL
        print(f'Downloading {full_link}')
        with requests.get(full_link, stream=True) as r:
            r.raise_for_status()
            with open(os.path.basename(file_link), 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192): 
                    f.write("data/"+chunk)

