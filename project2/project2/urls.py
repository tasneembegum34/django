
from django.contrib import admin
from django.urls import path
from srac import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('myhome/', views.home,name='home'),
    path('concatenate.*/',views.concatenate,name='concatenate'),
    
]
