from django.shortcuts import render

# Create your views here.

from django import http

def index(request):
    # return http.HttpResponse('This is my first Django Html page!')

    #使用模板
    # return render(request,'home.html')

    con = {'name':'Tom','age':'19'}
    return render(request,'home_arg.html',context=con)

