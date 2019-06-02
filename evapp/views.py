from django.shortcuts import render,redirect
from .forms import RegisterForm
# Create your views here.


def SignUpView(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return redirect("index")
    else:
        form = RegisterForm()
    return render(request, 'signup.html', { 'form': form })
