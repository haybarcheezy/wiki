from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:name>", views.entry, name="entry"),
    path("search_entry", views.search_entry, name="search_entry"),
    path("new_page", views.new_page, name="new_page"),
    path("random_page", views.random_page, name="random_page"),
    path("edit/<str:title>", views.edit_page, name="edit_page")
]
