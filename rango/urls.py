<<<<<<< HEAD
from django.conf.urls import url
from rango import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about')
]
=======
from django.conf.urls import url
from rango import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
>>>>>>> 3ff2dfde0f87c58d4c2d510f8e463658dda9e569
