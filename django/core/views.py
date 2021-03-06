from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Movie, Person
# Create your views here.

class MovieDetail(DetailView):
    queryset = (Movie.objects.all_with_related_persons())


class ModelListView(ListView):
    model = Movie
    paginate_by = 10


class PersonDetail(DetailView):

    queryset = Person.objects.all_with_prefetch_movies()

