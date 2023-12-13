from django.shortcuts render 
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, Det
from .models import Author
from django.urls import reverse_lazy


# Create your views here.
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
from .models import Author
from django.urls import reverse_lazy

class AuthorListView(ListView):
    model = Author

class AuthorDetailView(DetailView):
    model = Author

class AuthorCreateView(CreateView):
    model = Author
    fields = ['name', 'birth_date', 'pseudonym']

class AuthorUpdateView(UpdateView):
    model = Author
    fields = ['name', 'birth_date', 'pseudonym']

class AuthorDeleteView(DeleteView):
    model = Author
    success_url = reverse_lazy('author-list')

