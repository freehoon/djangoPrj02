from django.shortcuts import render

from django.views.generic.list import ListView
from .models import Board

class BoardListView(ListView):
    model = Board
    
# Create your views here.
