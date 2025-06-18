from django.shortcuts import render
from .models import Movie, Director
from django.http import JsonResponse
from django.core import serializers

def get_all_movies(request):
    all_movies = serializers.serialize("json", format=str ,Movie.objects.all()) 
    return JsonResponse(all_movies, safe=False)
# Create your views here.
