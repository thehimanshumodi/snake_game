from django.shortcuts import render

# Create your views here.
def game(request):
    return render(request, 'snake/game.html')