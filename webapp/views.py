from django.shortcuts import render

# Create your views here.
import json
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as django_logout
from django.http import HttpResponseRedirect
from .models import Product

def logout(request):
    django_logout(request)
    domain = 'dev-n6167-al.au.auth0.com'
    client_id = 'bau527h3kzqASeTNVcYzZF46R69qROuq'
    return_to = 'http://localhost:8000'
    return HttpResponseRedirect(f'https://{domain}/v2/logout?client_id={client_id}&returnTo={return_to}')

@login_required
def profile(request):
    user = request.user
    auth0user = user.social_auth.get(provider='auth0')
    userdata = {
        'user_id': auth0user.uid,
        'name': user.first_name,
        'picture': auth0user.extra_data['picture']
    }

    return render(request, 'webapp/profile.html', {
        'auth0User': auth0user,
        'userdata': json.dumps(userdata, indent=4)
    })

def index(request):
    products = Product.objects.all()

    context = {
        'products':products,
    }

    return render(request, 'webapp/index.html', context)
    