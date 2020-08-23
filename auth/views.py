from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic


def home(request):
    return render(
        request,
        'home.html'
    )


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

# def signup(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#         username = form.cleaned_data.get('username')
#         my_password = form.cleaned_data.get('password1')
#         user = authenticate(username=username, password=my_password)
#         login(request, user)
#         return redirect('login')
#     else:
#         form = UserCreationForm()
#         return render(request, 'signup.html', {'form': form})

