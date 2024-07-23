from django.shortcuts import redirect, render, get_object_or_404
from .models import Product, Category, CartItem
from django.contrib.auth.decorators import login_required

def home(request, category=None):
    if category:
        try:
            category_obj = Category.objects.get(name=category)
            products = Product.objects.filter(category=category_obj)
        except Category.DoesNotExist:
            products = []
    else:
        products = Product.objects.filter(category=1)
    return render(request, 'products/home.html', {'products': products, 'current_category': category})


def add_to_cart(request, product_id):
    if not request.user.is_authenticated:
        return redirect('signin')
    product = get_object_or_404(Product, id=product_id)
    cart_item, created = CartItem.objects.get_or_create(user=request.user, product=product)
    # Assuming you have a quantity field in your CartItem model
    if not created:
        cart_item.quantity += 1
    cart_item.save()
    return redirect('home')

def cart_view(request):
    if not request.user.is_authenticated:
        return redirect('signin')

    # Fetch cart items for the logged-in user
    cart_items = CartItem.objects.filter(user=request.user)
    print(f"User: {request.user}, Cart Items: {cart_items}")  # Debugging line
    return render(request, 'cart.html', {'cart_items': cart_items})

def payment(request):
    return render(request, 'payment.html')

@login_required
def clear_cart(request):
    CartItem.objects.filter(user=request.user).delete()
    return redirect('cart')

@login_required
def add_to_cart_multiple(request):
    if request.method == 'POST':
        for key, value in request.POST.items():
            if key.startswith('quantity_'):
                product_id = int(key.split('_')[1])
                quantity = int(value)
                if quantity > 0:
                    product = get_object_or_404(Product, id=product_id)
                    cart_item, created = CartItem.objects.get_or_create(user=request.user, product=product)
                    if created:
                        cart_item.quantity = quantity
                    else:
                        cart_item.quantity += quantity
                    cart_item.save()
    return redirect('home')
