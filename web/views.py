from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect

def index(request):

    return render(request, 'web/index.html')

def about(request):

    return render(request, 'web/about.html')

def contact(request):

    return render(request, 'web/Contact.html')


def product(request):

    return render(request, 'web/product.html')
