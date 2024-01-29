from django.shortcuts import render
from django.http import HttpResponse 
from .models.product import Product
def home(request):
    products =Product.get_all_products()
    #print(products)
    return render(request,'home.html',{'product':products})