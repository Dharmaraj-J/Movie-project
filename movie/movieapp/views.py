from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,Http404
from .models import Movie




def index(request):

    movies =  Movie.objects.all()
    # Movie.objects.filter()
    # Movie.objects.get() get one object


    return render(request,'index.html',{'movies':movies})


    # output = ','.join([m.title for m in movies])
    # return HttpResponse(output)


def detail(request,movie_id):
    # try:
       movie = get_object_or_404(Movie ,pk=movie_id)
       return render(request,'detail.html',{'movie':movie})
    # except Movie.DoesNotExist:
    #     raise Http404
