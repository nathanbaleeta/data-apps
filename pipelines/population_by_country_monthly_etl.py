#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
<File Name>:  Population by country monthly etl

<Author>: Nathan Baleeta
<Created>: 2025-12-29
<Version>: 1.0.0
<License>: MIT

<Description>:
An etl pipeline that collects global country population metrics
from worldometers, transforms the data and creates a curated dataset
ready for visualization
"""
__author__ = "Nathan Baleeta"
__version__ = "1.0.0"

import pandas as pd
import requests
from bs4 import BeautifulSoup

POPULATION_URL = "https://www.worldometers.info/world-population/population-by-country/"


def extract():
    response = requests.get(POPULATION_URL)
    soup = BeautifulSoup(response.content, 'html.parser')

    #Assuming the table ID/class is identified
    table = soup.find('table', {'class': 'datatable w-full border border-zinc-200'})

    data = []
    for row in table.find_all('tr')[1:]: # Skip the header row
        cols = row.find_all('td')
        if len(cols) > 2:
            country = cols[1].text.strip()
            population = cols[2].text.strip()
            yearly_change = cols[3].text.strip()
            land_area_sq_km = cols[6].text.strip()
            fertility_rate = cols[8].text.strip()
            urban_population_pct = cols[10].text.strip()

            data.append((country, population, yearly_change, land_area_sq_km, \
                         fertility_rate, urban_population_pct))
            
    df = pd.DataFrame(data, columns=['country', 'population', \
                                      'yearly_change', 'land_area_sq_km', \
                                      'fertility_rate', 'urban_population_pct'
                                      ])
    
    return len(df)




    

if __name__ == "__main__":
    result = extract()
    print(result)