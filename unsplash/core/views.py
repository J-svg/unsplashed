from django.shortcuts import render, HttpResponse
import requests
import json

def home(request):

    random = ['nature', 'love']
    payload = {
        'query': random,
        'count': 15,
        'client_id': ACCESS_KEY
    }
    url = 'https://api.unsplash.com/photos/random'
    r = requests.get(url, params=payload).json()

    package = json.dumps(r, indent=2)
    print(type(r))
    # print(package)

    arr = []
    for data in r:
        arr.append(data['urls']['regular'])

    context = {
        'link': arr,
    }
    # output = " ".join(arr)
    # return HttpResponse(output)
    return render(request, 'core/home1.html', context)


def search(request):
    
    place = request.GET.get('q')
    payload = {
        'query': place,
        'client_id': ACCESS_KEY,
        'per_page': 50,
    }
    url = 'https://api.unsplash.com/search/photos'
    r = requests.get(url, params=payload).json()

    package = json.dumps(r, indent=2)
    print(type(r['results']))
    print(len(r['results']))
    arr = []
    for data in r['results']:
        arr.append(data['urls']['regular'])

    context = {
        'link': arr,
    }
    #output = " ".join(arr)
    #return HttpResponse(output)
    return render(request, 'core/home1.html', context)