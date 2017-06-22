# from django.http import Http404
# from .models import Album , Song
# from django.shortcuts import render , get_object_or_404
# def index (request):
# 	all_albums= Album.objects.all()
# 	return render(request , "music/index.html",{"albums": all_albums })

# def detail(request, album_id):
# 	# try : 
# 	# 	album= Album.objects.get (id = album_id)
# 	# except :
# 	# 	raise Http404("Oops, that album does not exist")
# 	album = get_object_or_404(Album, pk=album_id)
# 	songs = album.song_set.all()
# 	return render(request , "music/detail.html",{"album": album ,"songs": songs } )

# def faveroute(request, album_id):
# 	# try : 
# 	# 	album= Album.objects.get (id = album_id)
# 	# except :
# 	# 	raise Http404("Oops, that album does not exist")
# 	# album = get_object_or_404(Album, pk=album_id)
# 	# songs = album.song_set.all()
# 	# return render(request , "music/detail.html",{"album": album ,"songs": songs } )
# 	# song = Song.objects.get(id=song_id)	
# 	# if song.faveroute:
# 	# 	song.faveroute= False
# 	# else: 
# 	# 	song.faveroute = True
# 	# song.save()
# 	album = get_object_or_404(Album , pk=album_id)
# 	try :
# 		selected_song = album.song_set.get(pk=request.POST['song'])
# 	except (KeyError, Song.DoesNotExist):
# 		return render(request , "music/detail.html",{"album": album  ,"error_message":"you did not select a valid song", }  )
# 	else :
# 		selected_song.is_faveroute = True
# 		selected_song.save()
# 		return render(request , "music/detail.html",{"album": album } )


from django.views import generic
from django.views.generic.edit import CreateView , UpdateView , DeleteView
from .models import Album
from django.core.urlresolvers import reverse_lazy

class IndexView(generic.ListView):
	template_name="music/index.html"
	context_object_name="albums"
	def get_queryset(self):
		return Album.objects.all()

class DetailView(generic.DetailView):
	model = Album
	template_name= "music/detail.html"


class AlbumCreate (CreateView):
	model = Album 
	fields=["artist","album_title","genre","album_logo"]

class AlbumUpdate (UpdateView):
	model = Album 
	fields=["artist","album_title","genre","album_logo"]
	

class AlbumDelete (DeleteView ):
	model = Album 
	success_url=reverse_lazy('music:index')
	# fields=["artist","album_title","genre","album_logo"]
