from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    # return HttpResponse("Covid-19 Data Platform")
    context_dict = {}
    return render(request, 'covid/index.html', context=context_dict)
