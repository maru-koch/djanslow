from django.urls import path
from core.views import index_view

urlpatterns=[
    path('', index_view, name='home')
]
