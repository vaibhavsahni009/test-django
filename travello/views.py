from django.shortcuts import render
from .models import destination
# Create your views here.



ds=destination.objects.all()

def index(request):
    return render(request,'index.html',{'ds':ds})