from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
def home_view(request,*args,**kwargs):
  #  return HttpResponse("<h1>hello world</h1>") 
  return render(request, "home.html",{})
def about_page(request,*args,**kwargs):
  my_context={
    "my_text": "this is about me" ,
    "my_number": 9120614410 ,
    "my_list" :[123,155,'abc']
  }
  #  return HttpResponse("<h1>hello world</h1>") 
  return render(request, "about.html",my_context)
def contact_page(request,*args,**kwargs):
  #  return HttpResponse("<h1>hello world</h1>") 
  return render(request, "contact.html",{})

