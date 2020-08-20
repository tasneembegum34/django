from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import operator

def family(requests):
    return HttpResponse('<h1><ul><li>Mother:9125673990</li><li>Father:7348040387</li><li>Brother:8576967292</li></ul></h1>')
def friends(requests):
    return HttpResponse('<h1><ul><li>Friend-1:6074245670</li><li>Friend-2:9605745490</li></ul></h1>')
