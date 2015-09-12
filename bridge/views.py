from django.shortcuts import render
from django.http import HttpResponse
import requests
import json
from django.views.decorators.http import require_http_methods

from bridge.models import Bridge
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
@require_http_methods(["POST"])
def index(request):
    if not all(x in request.POST for x in ['token', 'text','user_name','user_id']):
        return HttpResponse("")

    if request.POST['user_id'] == 'USLACKBOT':
        return HttpResponse("")

    b = Bridge.objects.get(source_token=request.POST['token'])
    if b is not None:
        #found a bridge
        url = b.destination_url.strip()
        payload = {'text': request.POST['text'], 'channel': b.destination_channel ,
                    'username': request.POST['user_name']}
        headers = {'content-type': 'application/json'}
        response = requests.post(url, data=json.dumps(payload), headers=headers)

    return HttpResponse("")