from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('add_book', views.add_book),
    path('view_book/<int:book_id>', views.view_book),
    path('add_to_book', views.add_to_book),
    path('authors', views.authors),
    path('add_author', views.add_author),
    path('view_author/<int:author_id>', views.view_author),
    path('add_to_author', views.add_to_author),
]