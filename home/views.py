from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')
def package(request):
    return render(request, 'package.html')
def about(request):
    return render(request, 'about.html')
def contact(request):
    return render(request, 'contact.html')

