from .views import *
from django.urls import path

"""All urls of web app
"""
urlpatterns = [
    path('register/', RegisterView.as_view(), name='user-register'),
    path('login/', LoginView.as_view(), name='user-login'),
    path('',LoginView.as_view(), name='user-login'),
    path('news/', NewsView.as_view(), name='news'),
    path('searches/', SearchView.as_view(), name="user-search"),
    path('existingview/<str:keyword>/', ExistingNewsView.as_view(), name="existing-view"),
    path('logout/', LogoutView.as_view(), name="user-logout"),
    path('admin-dash/', AdminDash.as_view(), name='admin-dash')
]
