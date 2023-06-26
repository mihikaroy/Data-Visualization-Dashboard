import json
from .models import Data

def load_data():
    with open(r'C:\\Users\roych\Downloads\jsondata.json') as file:
        data = json.load(file)

    for item in data:
        Data.objects.create(
            intensity=item['Intensity'],
            likelihood=item['Likelihood'],
            relevance=item['Relevance'],
            year=item['Year'],
            country=item['Country'],
            topics=item['Topics'],
            region=item['Region'],
            city=item['City']
        )
