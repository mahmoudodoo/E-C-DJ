from django.shortcuts import render,redirect
from .models import Item
# Create your views here.


def home(request):
    context = {
        'items': Item.objects.all()
    }

    print(context)
    return render(request,'home.html',context=context)



def create_item(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        price = request.POST.get('price')
        discount_price = request.POST.get('discount_price', 0)  # Default to 0 if not provided
        category = request.POST.get('category')
        label = request.POST.get('label')
        slug = request.POST.get('slug')
        description = request.POST.get('description')
        image = request.FILES.get('image')  # Get the uploaded file

        # Create and save the new item
        item = Item(
            title=title,
            price=float(price),
            dsicount_price=float(discount_price),
            category=category,
            label=label,
            slug=slug,
            description=description,
            image=image
        )
        item.save()
        
        return redirect('frontend:home')  # Redirect to home after creation

    return render(request, 'create_item.html')