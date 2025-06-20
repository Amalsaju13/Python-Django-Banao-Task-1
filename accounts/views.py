from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import CustomUserCreationForm
from .models import CustomUser
from django.contrib.auth.decorators import login_required

# Create your views here.

def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            if user.user_type == 'doctor':
                return redirect('doctor_dashboard')
            else:
                return redirect('patient_dashboard')
        else:
            return render(request, 'accounts/login.html', {'error': 'Invalid credentials'})
    return render(request, 'accounts/login.html')

@login_required
def doctor_dashboard(request):
    return render(request, 'accounts/doctor_dashboard.html', {'user': request.user})

@login_required
def patient_dashboard(request):
    return render(request, 'accounts/patient_dashboard.html', {'user': request.user})

def logout_view(request):
    logout(request)
    return redirect('login')
