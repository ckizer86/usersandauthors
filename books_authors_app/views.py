from django.shortcuts import render, redirect, HttpResponseRedirect
from .models import Book, Author

# Create your views here.
def index(request):

    context = {
        "all_books": Book.objects.all(),
        "all_authors": Author.objects.all(),
    }

    return render(request, "index.html", context)

def add_book(request):

    title = request.POST['booktitle']
    description = request.POST['bookdescription']

    Book.objects.create(title=title, desc=description)

    return redirect('/')

def view_book(request, book_id):
    this_book = Book.objects.get(id=book_id)

    context = {
            "book": this_book,
            "authors": this_book.publishers.all(),
            "exauthors": Author.objects.exclude(books=book_id),
        }


    return render(request, "view_book.html", context)

def add_to_book(request):
    book_id = request.POST['bookid']
    this_book = Book.objects.get(id=book_id)
    author_id = request.POST['author']
    this_author = Author.objects.get(id=author_id)
    this_author.books.add(this_book)
    next = request.POST.get('next', '/')

    return HttpResponseRedirect(next)

def authors(request):

    context = {
        "all_books": Book.objects.all(),
        "all_authors": Author.objects.all(),
    }

    return render(request, "authors.html", context)

def add_author(request):
    
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    notes = request.POST['notes']
    next = request.POST.get('next', '/')

    Author.objects.create(first_name=first_name, last_name=last_name, notes=notes)

    return HttpResponseRedirect(next)

def view_author(request, author_id):
    this_author = Author.objects.get(id=author_id)

    context = {
            "author": this_author,
            "books": this_author.books.all(),
            "exbooks": Book.objects.exclude(publishers=author_id),
        }


    return render(request, "view_author.html", context)

def add_to_author(request):
    author_id = request.POST['authorid']
    this_author = Author.objects.get(id=author_id)
    book_id = request.POST['book']
    this_book = Book.objects.get(id=book_id)
    this_book.publishers.add(this_author)
    next = request.POST.get('next', '/')

    return HttpResponseRedirect(next)