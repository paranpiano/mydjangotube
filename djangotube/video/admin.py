# video/admin.py
from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Video


class VideoAdmin(admin.ModelAdmin):
    list_display = ['title', 'video_key', 'link']

    def link(self, video):
        return mark_safe('<a href="https://www.youtube.com/watch?v={}" target="_black">link</a>'.format(video.video_key))

admin.site.register(Video, VideoAdmin)