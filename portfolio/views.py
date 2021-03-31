from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseRedirect
from django.urls.base import reverse_lazy
from django.conf import settings

# Create your views here.
def portfolio_cv(request):
    return render(request, 'cv_portfolio.html')