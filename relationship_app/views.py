from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required, permission_required
from django.views.generic import ListView, DetailView
from .models import Author, Book, Library, Librarian

# -----------------------
# Home view
# -----------------------
def home(request):
    user = request.user if request.user.is_authenticated else None
    return render(request, 'home.html', {'user': user})


# -----------------------
# Function-based Views (FBVs)
# -----------------------
@login_required(login_url='login')
def list_books(request):
    books = Book.objects.all()
    return render(request, 'list_books.html', {'books': books})


@login_required(login_url='login')
def list_authors(request):
    authors = Author.objects.all()
    return render(request, 'list_authors.html', {'authors': authors})


# -----------------------
# Class-based Views (CBVs)
# -----------------------
class BookListView(ListView):
    model = Book
    template_name = 'book_list.html'


class AuthorDetailView(DetailView):
    model = Author
    template_name = 'author_detail.html'


# -----------------------
# Authentication Views
# -----------------------
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')
    return render(request, 'logout.html')


# -----------------------
# Role-Based Access Control & Custom Permissions
# -----------------------
@permission_required('relationship_app.can_add_book', login_url='login')
def add_book_view(request):
    return HttpResponse("You have permission to add a book!")


@permission_required('relationship_app.can_edit_book', login_url='login')
def edit_book_view(request):
    return HttpResponse("You have permission to edit a book!")


@permission_required('relationship_app.can_delete_book', login_url='login')
def delete_book_view(request):
    return HttpResponse("You have permission to delete a book!")

