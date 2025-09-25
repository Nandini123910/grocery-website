from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
from .models import *
from django.contrib.auth.decorators import login_required
from cart.cart import Cart


# Create your views here.
def index(request):
    product=Product.objects.all()
    return render(request,'index.html',{'product':product})

def Signup(request):
    return render(request,'signup.html')

def Signin(request):
    return render(request,'signin.html')

def Signuppage(request):
    if request.method=='POST':
        uname=request.POST['username']
        email=request.POST['email']
        pwd=request.POST['password']

        try:
            user=User.objects.get(username=uname)
            return render(request,'signup.html',{'error':"username already exist"})
        except:
            user=User.objects.create_user(username=uname,email=email,password=pwd)
            user.save()
            return render(request,'index.html',{'msg':"Account Created"})
    else:
        return render(request,'signup.html',{'error':"invalid user request"})    
    

def Signinpage(request):
    if request.method=='POST':
        uname=request.POST['username']
        pwd=request.POST['password']
        user=auth.authenticate(username=uname,password=pwd)
        if user is not None:
            auth.login(request,user)
            return render(request,'index.html',{'msg':"user login successfully"})
        else:
            return render(request,'signin.html',{'error':"invalid password or username"})
    else:
            return render(request,'signin.html',{'error':"invalid password or username"})
    
def cart(request):
    return render(request,'cart.html')

@login_required(login_url="/users/login")
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect('cart')

@login_required(login_url="/users/login")
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect('cart')

@login_required(login_url="/users/login")
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect('cart')

@login_required(login_url="/users/login")
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect('cart')

@login_required(login_url="/users/login")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect('cart')

@login_required(login_url="/users/login")
def cart_detail(request):
    return render(request, 'cart/cart.html')
