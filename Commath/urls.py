from django.contrib import admin
from django.urls import path
from mysite import views

urlpatterns = [
    path('', views.index),
    path('admin/', admin.site.urls),
    path('32bit/', views.decto32fp),
    path('64bit/', views.decto64fp),
    path('AxBs/', views.AxBs),

    path('Differentiation/', views.differentiation),
    path('Integration/', views.integration),
    path('Rootfinding/', views.rootfinding),
]
