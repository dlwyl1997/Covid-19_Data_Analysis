from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    # return HttpResponse("Covid-19 Data Platform")
    context_dict = {}
    return render(request, 'index.html', context=context_dict)


def about(request):
    return render(request, 'about.html')


def info(request):
    return render(request, 'info.html')


def analysis(request):
    return render(request, 'covid/analysis.html')


def prediction(request):
    return render(request, 'covid/prediction.html')


def dataframe(request):
    return render(request, 'covid/dataframe.html')
