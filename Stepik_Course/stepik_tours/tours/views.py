from django.shortcuts import render
from django.http import HttpResponseNotFound, HttpResponseServerError
from random import randint
from .data import tours, departures


def main_view(request):
    tours_random = {}
    while len(tours_random) < 6:
        a = randint(1, 16)
        if a in tours_random:
            continue
        else:
            tours_random[a] = tours[a]
    context = {"tours_random": tours_random}
    return render(request, 'tours/index.html', context=context)


def departure_view(request, departure: str):
    tour_id = {}
    for i, y in tours.items():
        if y["departure"] == departure:
            tour_id[i] = y
    sums = []
    night = []
    for i, y in tour_id.items():
        sums.append(y["price"])
        night.append(y["nights"])
    context = {"id": departures[departure], "tour_id": tour_id, "sums_min": min(sums), "sums_max": max(sums),
               "night_min": min(night), "night_max": max(night)}
    return render(request, 'tours/departure.html', context=context)


def tour_view(request, id: int):
    context = {"tours": tours[id]}
    return render(request, 'tours/tour.html', context=context)


def custom_handler404(request, exception):
    return HttpResponseNotFound('Страницы не существует!')


def custom_handler500(request):
    return HttpResponseServerError('Ошибка сервера!')
