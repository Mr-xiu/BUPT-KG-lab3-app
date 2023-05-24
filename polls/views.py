import json

# Create your views here.
from django.http import JsonResponse


def index(request):
    print('request', request)
    with open('database/entity_result.json', 'r', encoding="UTF8") as f:
        entity_list = json.load(f)

    return JsonResponse(entity_list, safe=False)
