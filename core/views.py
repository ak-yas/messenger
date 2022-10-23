from django.shortcuts import render


def home_screen(request, *args, **kwargs):
    context = {}
    return render(request, "core/home.html", context)