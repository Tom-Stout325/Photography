from django.urls import path
from .views import *
from accounts.views import Home
from accounts import *


urlpatterns = [
    path('', Home, name='home'),
    path('studio/', StudioView.as_view(), name='studio'),
]
