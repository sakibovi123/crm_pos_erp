from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.contrib.auth.hashers import make_password, check_password
# Create your views here.


def get_registration_page_for_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email')
        password = request.POST.get('password')
        profile_picture = request.FILES.get('profile_picture')

        register = UserModel(
            username=username,
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number,
            email=email,
            password=make_password(password),
            profile_picture=profile_picture,
        )

        register.save()

        # success = register.save()

        return redirect("UserLogin")


    args = {}
    return render(request, 'registration.html', args)


def get_login_for_user(request):
    msg = None
    if request.method == "POST":
        username = request.POST.get('username')
        print(username)
        password = request.POST.get('password')
        user = UserModel.get_username(username)
        print(str(user))
        if user:
            match = check_password(password, user.password)
            if match:
                request.session['user'] = user.__dict__
                return HttpResponse("Succesffully Logged in")
            else:
                msg = "Username or password doesnt match on our record"
        else:
            msg = "User not found"

    args = {
        "msg": msg
    }
    return render(request, "login.html", args)