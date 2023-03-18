from django.shortcuts import render
from django.http import HttpResponse
from .models import Member
# Create your views here.


def members(request):
    mymembers = Member.objects.all().values()
    return render(request, 'allmembers.html', {'mymembers': mymembers })


def details(request, id):
    mymembers = Member.objects.get(id=id)
    return render(request, 'details.html', {'mymembers': mymembers})


def main(request):
     return render (request, 'main.html')


def testing(request):
    fruits = ['Apple', 'Banana', 'Cherry']
    return render(request, 'template.html', {'fruits': fruits})





