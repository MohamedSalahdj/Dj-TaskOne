from django.urls import path
from .views import home, list_tracks, track_details

urlpatterns = [
    path('', home),
    path('tracks/', list_tracks),
    path('tracks/<str:name>', track_details)
]