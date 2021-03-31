from django.urls import path, re_path
from django.conf.urls import url
from portfolio import views as portfolio_views

app_name="master"
urlpatterns = [ path('', portfolio_views.portfolio_cv, name='portfolio'),
    ]