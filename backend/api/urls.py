from django.urls import path

from .views import IndexPageView


app_name = 'api'

urlpatterns = [
    path('menu/', IndexPageView.as_view(), name='index')
]
