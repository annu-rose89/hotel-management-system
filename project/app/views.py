
from django.shortcuts import render, redirect,get_object_or_404

from .forms import BookingForm
from .models import Booking

def login(request):
    if request.method == "POST":
        return redirect('home')
    return render(request, 'login.html')

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')


def rooms(request):
    return render(request, 'rooms.html')

def services(request):
    return render(request, 'services.html')

def gallery(request):
    return render(request, 'gallery.html')


def bookings(request):
    if request.method == "POST":

        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        address = request.POST.get('address')
        members = request.POST.get('members')
        days = request.POST.get('days')
        room_type = request.POST.get('room_type')
        gender = request.POST.get('gender')
        payment_method = request.POST.get('payment_method')


        Booking.objects.create(
            name=name,
            phone=phone,
            email=email,
            address=address,
            members=members,
            days=days,
            room_type=room_type,
            gender=gender,
            payment_method=payment_method
        )

        return redirect('success')

    return render(request, 'bookings.html')



def success(request):
    return render(request, 'success.html')


def contact(request):
    return render(request, 'contact.html')


def mybookings(request):
    bookings = Booking.objects.all()
    return render(request, 'mybookings.html', {'bookings': bookings})



def dashboard(request):
    return render(request, 'dashboard.html')

def admin_dashboard(request):
    bookings = Booking.objects.all()
    return render(request, 'admin_dashboard.html', {'bookings': bookings})


def logout(request):
    return redirect('login')


def dashboard(request):

    bookings = Booking.objects.all()

    return render(request, 'dashboard.html', {'bookings': bookings})


def edit_Booking(request, id):
    booking = get_object_or_404(Booking, id=id)

    if request.method == 'POST':
        booking.name = request.POST.get('name')
        booking.phone = request.POST.get('phone')
        booking.email = request.POST.get('email')
        booking.address = request.POST.get('address')
        booking.days = request.POST.get('days')
        booking.members = request.POST.get('members')
        booking.save()

        return redirect('dashboard')

    return render(request, 'edit_booking.html', {'booking': booking})

# DELETE BOOKING
def delete_booking(request, id):

    booking = get_object_or_404(Booking, id=id)

    booking.delete()

    return redirect('dashboard')
def single_booking(request,id):
    profile=Booking.objects.get(id=id)
    return render(request,'single_booking.html',{'profile':profile})






