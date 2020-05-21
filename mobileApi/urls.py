from django.urls import path
from .views import apiOverView
from . import views

urlpatterns = [
    path('', views.apiOverView, name='api_overview'),
    path('details-List/', views.detailsList, name='details-List'),

]
