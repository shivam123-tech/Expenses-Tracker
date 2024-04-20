#from django.conf.urls import url
from django.urls import path, include
from . import views 
from .views import logout_view

urlpatterns = [
    path('', views.home, name='home'),
    path('expenses', name='expenses', view=views.ExpenseListView.as_view()),
    path('accounts/register/', views.register, name='register'),
    path('accounts/', include('django.contrib.auth.urls')),
     path('logout/', logout_view, name='logout'),
]
