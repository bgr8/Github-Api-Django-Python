from django.shortcuts import render, HttpResponse, redirect
import json
import requests
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.
base_url = "https://api.github.com/users/"

def index(request):
    if request.method == "POST":

        githubname = request.POST.get("githubname")
        response_user = requests.get(base_url + githubname)
        response_repos = requests.get(base_url + githubname + "/repos")

        user_info = response_user.json()
        repos = response_repos.json()
        message = response_user.json()
        

        if "message" in user_info:
            context = {
                'error': 'Kullanıcı bulunamadı....'
            }
            return render(request, 'index.html', context)
        else:      
            context = {
                'profile': user_info,
                'repos' : repos,
            }      
            return render(request, "index.html", context)
    else:
        return render(request, 'index.html')
