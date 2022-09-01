from django.shortcuts import render,HttpResponse
from home.models import Contact
# Create your views here.

def home(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        desc=request.POST['desc']
        ins=Contact(name=name,email=email,desc=desc)
        ins.save()
        print("data written")
    return render(request,'contact.html')