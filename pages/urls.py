# -*- coding: utf-8 -*-
"""


Vytvořeno dne Tue Aug  1 23:20:15 2023

@Autor: Karel Rečka
"""

# pages/urls.py
from django.urls import path
from .views import HomePageView, AboutPageView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("about/", AboutPageView.as_view(), name="about"),
]

