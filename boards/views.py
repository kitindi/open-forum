from django.shortcuts import render
from .models import Board

# Create your views here.


def index(request, *args, **kwargs):
    
    return render(request,'index.html' )


def home(request, *args, **kwargs):
    boards = Board.objects.all()
    return render(request, 'home.html',{'boards': boards})