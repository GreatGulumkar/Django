from django.shortcuts import render, redirect
from django.contrib import messages
from .models import UserProfile
import logging

# rest_framework imports
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response


@csrf_exempt
@api_view(["POST", "GET", "PUT"])
def user_login(request):
    print("----->Entered login")
    if request.method == "POST":
        print(
            "==============>>>>>>>>", request.data["username"], request.data["password"]
        )  # .get("username"))
        if UserProfile.objects.filter(
            username=request.data["username"], password=request.data["password"]
        ):
            htmlusername = request.data["username"]
            print(htmlusername)
            return redirect(f"/?username={htmlusername}")
    return render(request, "login.html")


@csrf_exempt
@api_view(["POST", "GET", "PUT"])
def user_register(request):
    if request.method == "POST":
        # print(request.data["username"], request.data["email"], request.data["password"])
        UserProfile.objects.create(
            username=request.data["username"],
            email=request.data["email"],
            password=request.data["password"],
        )
        return redirect("user_login")

    return render(request, "register.html")
