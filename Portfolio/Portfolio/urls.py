
from django.contrib import admin
from PortfolioApp import views
from django_distill import distill_path
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    distill_path(
        '', 
        views.index, 
        name='index',
        distill_file='index.html'
    ),
]


