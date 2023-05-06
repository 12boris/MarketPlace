from mainapp import views
from django.views.generic import RedirectView
from django.urls import path, include
import mainapp.views as mainapp


app_name = 'mainapp'

urlpatterns = [
    path("", mainapp.main, name="index"),
]
