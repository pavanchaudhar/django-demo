from django.contrib import admin
from django.urls import path
from mama import views

urlpatterns = [
   
    path('', admin.site.urls),
    path('', views.index,),
]
