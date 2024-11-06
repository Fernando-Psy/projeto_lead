from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Lead
from django.db.models import Count

@login_required
def dashboard(request):
    leads_by_date = Lead.objects.values('data_cadastro').annotate(total=Count('id')).order_by('-data_cadastro')
    return render(request, 'leads/dashboard.html', {'leads_by_date': leads_by_date})