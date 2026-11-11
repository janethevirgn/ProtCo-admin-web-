from django.shortcuts import render


def login_register_view(request):
    # Hayaan na ang JavaScript at LocalStorage ang humawak ng login/register flow
    return render(request, 'login.html')


def admin_dashboard(request):
    # Ang counts (reports logged / registered users) ay galing sa localStorage via static/js/protco.js
    return render(request, 'dashboard.html')


def reports(request):
    return render(request, 'reports.html')


def users(request):
    return render(request, 'users.html')


def windmap(request):
    return render(request, 'windmap.html')


def schoolmap(request):
    return render(request, 'schoolmap.html')


def settings_view(request):
    return render(request, 'settings.html')
