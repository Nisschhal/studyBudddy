from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import models
from . import forms

# Create your views here.


def home(request):
    rooms = models.Room.objects.all()
    return render(request, 'base/home.html', context={'rooms': rooms})


def room(request, pk):
    room = None
    for i in rooms:
        if i['id'] == int(pk):
            room = i
    context = {'room': room}
    return render(request, 'base/room.html', context)


def createRoom(request):
    form = forms.RoomForm()
    if request.method == 'POST':
        form = forms.RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'base/room_form.html', context)
