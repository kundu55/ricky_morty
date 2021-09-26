import os
import requests

def get_data():
    url = 'https://rickandmortyapi.com/api/character'
    r = requests.get(url, headers={'Authorization':'Bearer %s' % os.getenv('DO_ACCESS_TOKEN')})
    data = r.json()
    data_list = []
    for i in range(len(data['results'])):
        data_list.append(data['results'][i])
    return data_list
