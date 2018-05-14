# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return render(request, "survey_app/index.html")

def process(request):
    if "count" not in request.session:
        request.session["count"] = 0
    request.session["count"] += 1

    if request.method == "POST":
        request.session["name"] = request.POST["name"]
        request.session["location"] = request.POST["location"]
        request.session["language"] = request.POST["language"]
        request.session["comment"] = request.POST["comment"]
    return redirect('/results')

def results(request):
    return render(request, "survey_app/results.html")

# Create your views here.
