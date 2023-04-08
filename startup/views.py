from django.shortcuts import render
import requests
import ast
# Create your views here.
def index(request):
    startups = requests.get(url='https://api.ecelliitr.org/edc/community?format=json')
    startups = ast.literal_eval(startups.text)
    return render(request, "startup/index.html", {
        "startups":startups
    })