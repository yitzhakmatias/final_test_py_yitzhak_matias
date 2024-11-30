from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from final_test.views import  custom_api

router = DefaultRouter()

urlpatterns = [
    path('api/custom/', custom_api),
]
