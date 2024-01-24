from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render
from django.contrib.messages import constants
from django.contrib import messages
from django.contrib.auth.models import User
from django.conf import settings
from django.urls import reverse


def signup(request: HttpRequest) -> HttpResponse | JsonResponse:
    match request.method:
        case 'GET':
            return render(request, 'signup.html')

        case 'POST':
            if '' in request.POST.values():
                return JsonResponse({
                    'success': False,
                    'message_text': 'Fill in all the fields on the form.',
                    'message_class': settings.MESSAGE_TAGS[constants.ERROR],
                })
            
            username = request.POST.get('username')
            password1 = request.POST.get('password1')
            password2 = request.POST.get('password2')

            # faça as verificações do formulario
            if password1 != password2:
                return JsonResponse({
                    'success': False,
                    'message_text': 'Passwords does not match.',
                    'message_class': settings.MESSAGE_TAGS[constants.ERROR],
                })
            
            user = User(username=username)
            user.set_password(password1)
            user.save()
            
            messages.add_message(request, constants.SUCCESS,'Successfully registered.')

            return JsonResponse({
                'success': True,
                'redirect_url': reverse('signin'),
            })

def signin(request: HttpRequest) -> HttpResponse | JsonResponse:
    match request.method:
        case 'GET':
            pass

        case 'POST':
            pass