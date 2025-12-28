from django.urls import path
from . import views

urlpatterns = [
    path("",views.index),
    path("<int:month_num>",views.month_by_num),
    path("<str:month_name>",views.monthly_challenge , name="month-name-challenge")
]

