from django.urls import path
from django.contrib.auth import views as auth_views
import accounts.views as view


urlpatterns = [
    path('register', view.register, name='register'),
    path('my_account', view.my_account, name='my_account'),
]