from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect, get_object_or_404
from myapp.models import Product
from myapp.my_forms import ProductForm

@login_required
def home(request):
    products = Product.objects.all() # select * from products
    return render(request, "home.html", {"products": products} )

@login_required
def add(request):
    if request.method == "POST":
        form  = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, f"{form.name} successfully added")
            return redirect('home')
    else:
        form = ProductForm()
    return render(request, "add.html", {"form": form})


    # Product.objects.create(name="Unga",
    #                        code="01008998",
    #                        price=510.0,
    #                        cost=488.0,
    #                        category="Foods",
    #                        for_sale=False
    #                        )

@login_required
def delete_product(request, id):
    product = Product.objects.get(id=id) # select * from products where id=65
    product.delete() # delete from products where id=65
    messages.warning(request, f"{product.name} deleted permanently")
    return redirect('home')


@login_required
def edit_product(request, id):
    product = Product.objects.get(id=id)
    if request.method == "POST":
        form  = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, f"{product.name} successfully updated")
            return redirect('home')
    else:
        form = ProductForm(instance=product)
    return render(request, "edit.html", {"form": form})

@login_required
def details(request,id):
    product = get_object_or_404(Product, id=id)
    return render(request, "details.html", {"product": product})

#group(perms)
def signin(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            messages.success(request, "Successfully logged in")
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})


def signup(request):
    return None

@login_required
def signout(request):
    if request.method == "POST":
        logout(request)
    return redirect('login')