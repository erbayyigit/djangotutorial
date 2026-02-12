from django.urls import path

from . import views #imports views.py file

urlpatterns=[
    path("", views.index, name="index"),
    path("chowder/", views.chowder, name="dog"),
    path("myfile/", views.serve_chowders_file, name="myfile")
]