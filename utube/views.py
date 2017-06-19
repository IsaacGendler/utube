from django.shortcuts import render

def video_list(request):
	 return render(request, 'utube/video_list.html', {})
