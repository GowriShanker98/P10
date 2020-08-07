from django.urls import path
from myapp import views
app_name="myapp"

urlpatterns = [
    path('index/',views.index,name="Index"),
    path('profile/',views.profile,name="Profile"),
]
