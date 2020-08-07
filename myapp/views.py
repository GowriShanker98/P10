from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<h1>Project is on AIR</h1>")

def base(request):
    return render(request,"_base.html")

def home(request):
    return render(request,"myapp/_home.html")

def profile(request):
    name="Pyspiders"
    return render(request,"myapp/_profile.html",{'name':name})