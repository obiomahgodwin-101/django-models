from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    # Function-based views
    path('books/', views.list_books, name='list_books'),
    path('authors/', views.list_authors, name='list_authors'),

    # Class-based views
    path('books/list/', views.BookListView.as_view(), name='book_list'),
    path('authors/<int:pk>/', views.AuthorDetailView.as_view(), name='author_detail'),

    # Authentication URLs
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # Role-Based Access URLs
    path('books/add/', views.add_book_view, name='add_book'),
    path('books/edit/', views.edit_book_view, name='edit_book'),
    path('books/delete/', views.delete_book_view, name='delete_book'),
]

