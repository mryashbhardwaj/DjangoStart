from django.http import Http404
from .models import Album
from django.shortcuts import render

def index (request):
	all_albums= Album.objects.all()
	return render(request , "music/index.html",{"albums": all_albums })

def detail(request, album_id):
	try : 
		album= Album.objects.get (id = album_id)
	except :
		raise Http404("Oops, that album does not exist")
	songs = album.song_set.all()
	return render(request , "music/detail.html",{"album": album ,"songs": songs } )
	
