from django.shortcuts import render
def mainpage(request):
 return render(request, 'pages/mainpage.html')


def mainpage(request):
 return render(request, 'pages/mainpage.html')


def enroll(request):
 return render(request, 'pages/enroll.html')

def login(request):
 return render(request, 'pages/login.html')

def about(request):
 return render(request, 'pages/about.html')

def faq(request):
 return render(request, 'pages/faq.html')

def service(request):
 return render(request, 'pages/service.html')
