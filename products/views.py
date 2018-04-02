from django.shortcuts import render
from .models import Product


def products_list(request):
    products = Product.objects.all()
    products = products.order_by('create_date')
    return render(request, 'products/product_list.html', {'products': products})