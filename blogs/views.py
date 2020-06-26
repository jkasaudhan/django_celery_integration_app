from django.shortcuts import render
from django.http import JsonResponse
from blogs.tasks import sleep_well

# Create your views here.
def get_blog(request):
    data = {
        'success': True,
        'message': 'simple api response'
    }
    sleep_well.delay(5)
    return JsonResponse(data)