from django.urls import path
from . import views

urlpatterns = [
    path('', views.accept, name="accept"),
    path('<int:id>/', views.resume, name="resume"),
]
