from django.shortcuts import render
from django.shortcuts import render
from .models import Tenants, Properties, Payments

def tenants_view(request):
    tenants = Tenants.objects.all()
    return render(request, 'tenants.html', {'tenants': tenants})

def properties_view(request):
    properties = Properties.objects.all()
    return render(request, 'properties.html', {'properties': properties})

def payments_view(request):
    payments = Payments.objects.all()
    return render(request, 'payments.html', {'payments': payments})

