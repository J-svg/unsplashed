from django.shortcuts import render, HttpResponse
import requests
import json

def home(request):
    ACCESS_KEY='YBBd6J15p1YwXIV3THzl4Zt3eHiD3BGT8unud0VUNQo'
    random = 'nature'
    payload = {
        'query': random,
        'count': 25,
        'client_id': ACCESS_KEY
    }
    url = 'https://api.unsplash.com/photos/random'
    r = requests.get(url, params=payload).json()

    package = json.dumps(r, indent=2)

    arr = []
    for data in r:
        arr.append(data['urls']['regular'])

    context = {
        'link': arr,
        'text': "Image Gallery:",
    }

    return render(request, 'core/home.html', context)


def search(request):
    ACCESS_KEY = 'YBBd6J15p1YwXIV3THzl4Zt3eHiD3BGT8unud0VUNQo'
    place = request.GET.get('q')
    payload = {
        'query': place,
        'client_id': ACCESS_KEY,
        'per_page': 50,
    }
    url = 'https://api.unsplash.com/search/photos'
    r = requests.get(url, params=payload).json()

    package = json.dumps(r, indent=2)
    arr = []
    for data in r['results']:
        arr.append(data['urls']['regular'])

    place=place.upper()+":"
    context = {
        'link': arr,
        'text': place,
    }
    return render(request, 'core/home.html', context)