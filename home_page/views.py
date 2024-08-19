from django.shortcuts import render

# Create your views here.
def home_page(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html',{
        'title':"About | Play Tailwind",
        'Banner':"About Us Page",
    })

def pricing(request):
    return render(request,'pricing.html',{
        'title':"Pricing | Play Tailwind",
        'Banner':"Pricing Page",
    })

def contact(request):
    return render(request,'contact.html',{
        'title':"Contact | Play Tailwind",
        'Banner':"Contact Us Page",
    })

def blog_grids(request):
    return render(request,'blog-grids.html',{
        'title':"Blog Grids | Play Tailwind",
        'Banner':"Blog Page",
    })

def blog_details(request):
    return render(request,'blog-details.html',{
        'title':"Blog Details | Play Tailwind",
        'Banner':"Blog Details Page",
    })

def signup(request):
    return render(request,'signup.html',{
        'title':"Sign Up | Play Tailwind",
        'Banner':"Sign Up Page",
    })

def signin(request):
    return render(request,'signin.html',{
        'title':"Sign In | Play Tailwind",
        'Banner':"Sign In Page",
    })

def page_not_found(request):
    return render(request,'404.html',{
        'title':"Page Not Found | Play Tailwind",
        'Banner':"Page Not Found",
    })

