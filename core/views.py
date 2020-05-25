from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return render(request, "general/home.html")

def about(request):
    return render(request, "core/about.html")

def login(request):
    return render(request, "accounts/login.html")

def screen(request):
    return render(request, "general/screen.html")

def chatbot(request):
    return render(request, "general/chatbot.html")