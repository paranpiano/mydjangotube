# video/views.py
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from .models import Video


def video_list(request):
    return render(request, 'video/video_list.html', {
        'video_list': Video.objects.all(),
        })

def video_detail(request, video_id):
    video = Video.objects.get(id=video_id)
    return render(request, 'video/video_detail.html', {'video': video})


def video_new(request):
    if request.method == 'POST':
        title = request.POST['title']
        video_key = request.POST['video_key']
        Video.objects.create(title=title, video_key=video_key)
        return redirect(reverse('video:list'))
    elif request.method == 'GET':
        return render(request, 'video/video_new.html')