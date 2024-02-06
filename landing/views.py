from django.shortcuts import render


def landing(request):
    return render(request, "index.html")


def login_button(request):
    return render(request, "login.html")
