from django.shortcuts import render

# Create your views here.


def home(request):
    context = {}
    return render(request, 'store/home.html', context)

def products(request):
    context = {}
    return render(request, 'store/products.html', context)

def brands(request):
    context = {}
    return render(request, 'store/brands.html', context)
#
# def cart(request):
#     context = {}
#     return render(request, 'main/cart.html', context)
#
# def checkout(request):
#     context = {}
#     return render(request, 'main/checkout.html', context)