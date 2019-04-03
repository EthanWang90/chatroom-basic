from django.urls import path
from .views import index, room
from django.conf.urls import url

app_name="chat"
urlpatterns = [
    path('', index, name='index'),
    url(r'^(?P<room_name>[^/]+)/$', room, name='room'),
]