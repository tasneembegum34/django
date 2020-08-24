from django.shortcuts import render
from django.http import HttpResponse

import operator
# Create your views here
def home(requests):
    return render(requests,'srac/home.html')
def concatenate(requests):
    mytext1=requests.GET['fulltext1']
    mytext2=requests.GET['fulltext2']
    mytext3=requests.GET['fulltext3']
    strings=[mytext1,mytext2,mytext3]
    #strings=mytext.split()
    l=[]
    r=" "
    for i in strings:
        l.append(i[::-1])
    for i in l:
        r=r+i
    return render(requests,'srac/concatenate.html',{'concatenate':r})
