from django.shortcuts import render , redirect,get_object_or_404
from farmcom.forms import CreateUserForm 

from django.contrib.auth import login
from django.contrib import messages

from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required 

def register(request):	
	form = CreateUserForm()

	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			form.save()
			user = form.cleaned_data.get('username')
			messages.success(request, 'Your Account has been created for '+ user)
			return redirect('farmcom:login_reg')


	context = { 'form': form }
	return render (request, 'signin/register.html', context)


def login_reg(request):

	if request.method =='POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(request, username = username, password = password)
		if user is not None:
			login(request, user)
			return redirect('farmcom:index.html')
		else:
			messages.info(request, "Username Or password is incorrect.")


	context = {}
	return render (request, 'signin/login.html', context)

def logoutuser(request):
	logout(request)
	return redirect('farmcom:login_reg')


@login_required(login_url = 'farmcom:login_reg')
def info(request):
	return render (request,"signin/info.html", context = {})
from django.shortcuts import render,redirect

# Create your views here.
def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def faq(request):
    return render(request,'faq.html')

def index_2(request):
    return render(request,'index_2.html')

def index(request):
    return render(request,'index.html')

def news_left_sidebar(request):
    return render(request,'news_left_sidebar.html')

def news_right_sidebar(request):
    return render(request,'news_right_sidebar.html')

def news_single(request):
    return render(request,'myaccount.html')
def pricing(request):
    return render(request,'pricing.html')

def projects_single(request):
    return render(request,'projects_single.html')

def projects(request):
    return render(request,'projects.html')

def service_single(request):
    return render(request,'service_single.html')

def services(request):
    return render(request,'services.html')

def team(request):
    return render(request,'team.html')

def testimonials(request):
    return render(request,'testimonials.html')

def typography(request):
    return render(request,'typography.html')



def submit(request):
    a = request.POST(['initial'])
    return render(request, 'home/home.html', {
        'error_message': "returned"
    })
from .forms import ProductForm, OrderForm
from .models import Product


def product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            img_obj = form.instance
            return render(request, 'imageapp\product.html', {'form': form, 'img_obj': img_obj})
    else:
        form = ProductForm()
    return render(request, 'imageapp\product.html', {'form': form})

def products(request):
    all_products=Product.objects.all()
    context={'all_products':all_products}
    return render(request, 'imageapp\products.html', context)

def order(request, id):
    obj = get_object_or_404(Product, id =id)
    form = OrderForm(request.POST or None, instance = obj)
    data = Product.objects.get(id = id)
    if form.is_valid():
        form.save()
        return redirect('farmcom:products')
    context = {'form':form, 'data':data}
    return render(request, 'imageapp/order.html', context)

def kart(request):
    Ordered_items = Product.objects.filter(order_status = True)
    print("Ordered Items :", Ordered_items)
    price = Product.objects.values('price')[0]
    total = 0
    total_value = 0
    for price in Ordered_items:
        print(price.price)
        print(price.items)
        total = price.price*price.items
        total_value = total_value+total
        print(total)

    print(total_value)
    context = {'Ordered_items':Ordered_items, 'total':total_value}
    return render(request, 'imageapp/kart.html', context)