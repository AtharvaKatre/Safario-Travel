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
def paris(request):
    return render(request, 'paris.html')
def cyprus(request):
    return render(request, 'cyprus.html')
def venice(request):
    return render(request, 'venice.html')
def tokyo(request):
    return render(request, 'tokyo.html')
def los_angeles(request):
    return render(request, 'los_angeles.html')
def prague(request):
    return render(request, 'prague.html')

