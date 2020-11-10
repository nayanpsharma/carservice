from django.shortcuts import render
from django.http import HttpResponse
from .models import Car
from django.http import Http404


def home(request):
    cars = Car.objects.all()
    return render(request, 'home.html', {'cars':cars})


def car_detail(request, id):
    try:
        car = Car.objects.get(id=id)
    except Car.DoesNotExist:
        raise('Car Not Found')

    return render(request, 'car_detail.html', {'car': car})




