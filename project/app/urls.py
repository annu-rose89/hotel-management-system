
from django.urls import path
from . import views

urlpatterns = [

    path('', views.login, name='login'),
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('rooms/', views.rooms, name='rooms'),
    path('services/', views.services, name='services'),
    path('gallery/', views.gallery, name='gallery'),

    path('bookings/', views.bookings, name='bookings'),
    path('success/', views.success, name='success'),  # 👈 ADD THIS

    path('contact/', views.contact, name='contact'),
    path('mybookings/', views.mybookings, name='mybookings'),

    path('logout/', views.logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),

   path('view/<int:id>/', views.dashboard, name='dashboard'),

    path('edit-booking/<int:id>/', views.edit_Booking, name='edit_Booking'),

    path('delete-Booking/<int:id>/', views.delete_booking, name='delete_Booking'),
    path('single-Booking/<int:id>', views.single_booking, name='single_Booking'),


]