<<<<<<< HEAD
from django.conf.urls import url
from django.shortcuts import render


from django.http import HttpResponse

def index(request):
    context_dict = {'boldmessage': "crunchy, creamy cookie, candy, cupcake!"}
    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    return render(request, 'rango/about.html', context = {})
=======
from django.conf.urls import url
from django.shortcuts import render


from django.http import HttpResponse

def index(request):
    context_dict = {'boldmessage': "crunchy, creamy cookie, candy, cupcake!"}
    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    return HttpResponse("Rango says here is the about page")
>>>>>>> 3ff2dfde0f87c58d4c2d510f8e463658dda9e569
