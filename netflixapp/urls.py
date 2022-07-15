from unicodedata import name
from django.urls import URLPattern, path
from .views import Home, ProfileCreate, ProfileList

app_name = 'netflixapp'

urlpatterns = [
    path('', Home.as_view(), name="Home"),
    path('profiles/', ProfileList.as_view(), name="profile-list"),
    path('profiles/', ProfileList.as_view(), name="profile-list"),
    path('profiles/create/', ProfileCreate.as_view(), name="profile-create"),
    
]
