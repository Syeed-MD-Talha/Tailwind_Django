from django.urls import path,include
from .import views

urlpatterns = [
    path('',views.home_page,name='home_page'),
    path('404/',views.page_not_found,name='page_not_found'),
    path('signin/',views.signin,name='signin'),
    path('signup/',views.signup,name='signup'),
    path('blog_details/',views.blog_details,name='blog_details'),
    path('blog_grids/',views.blog_grids,name='blog_grids'),
    path('contact/',views.contact,name='contact'),
    path('pricing/',views.pricing,name='pricing'),
    path('about/',views.about,name='about'),
]
