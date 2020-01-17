from django.urls import path
import home.views as view

urlpatterns = [
    path('', view.get_home, name='home'),
]