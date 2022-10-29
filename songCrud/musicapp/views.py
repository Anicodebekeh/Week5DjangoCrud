from django.http import HttpResponse

# Create your views here.

from django.http import HttpResponse


def index (request):
    return HttpResponse ("Hello, world. You're at the musicapp index.")
