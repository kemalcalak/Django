from datetime import date
from django.shortcuts import get_object_or_404, render
from movies.forms import CommentForm
from django.http.response import HttpResponseRedirect
from movies.models import Movie
from django.urls import reverse

data = {   
    "sliders": [
        {
            "slider_image": "slider1.jpg",
            "url": "film-adi-1"
        },
         {
            "slider_image": "slider2.jpg",
            "url": "film-adi-2"
        },
         {
            "slider_image": "slider3.jpg",
            "url": "film-adi-3"
        }
    ]
}

# Create your views here.

def index(request):
    movies = Movie.objects.filter(is_active=True,is_home=True)
    sliders = data["sliders"]
    return render(request, 'index.html', {
        "movies": movies,
        "sliders": sliders
    })

def movies(request):
    movies = Movie.objects.filter(is_active=True)
    return render(request, 'movies.html', {
        "movies": movies
    })

def movie_details(request, slug):
    movie = get_object_or_404(Movie, slug=slug)
    comment_form = CommentForm()

    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.movie = movie
            comment.save()
            return HttpResponseRedirect(reverse("movie_details", args=[slug]))

    return render(request, 'movie-details.html', {
        "movie": movie,
        "genres": movie.genres.all(),
        "people": movie.people.all(),
        "videos": movie.video_set.all(),
        "comment_form": comment_form
})