from django.contrib import admin
from django.urls import path
from cars.views import *
app_name = 'car'
urlpatterns = [
path('car/create/',CarCreateView.as_view() ),
path('all/', CarsListView.as_view()),
path('car/detail/<int:pk>/', CarDetailView.as_view()),
]
