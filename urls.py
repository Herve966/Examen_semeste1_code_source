


from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views  # Import de la vue de déconnexion
from django.shortcuts import redirect
from django.urls import path, include


# Redirection de la page d'accueil vers la page de login
def redirect_to_login(request):
    return redirect('login')  # Assurez-vous que 'login' correspond bien à l'URL de connexion définie

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', redirect_to_login),  # Redirige la page d'accueil vers la page de login
    path('login/', include('registration.urls')),  # URL de la page de connexion
    path('supplier/', include('supplier.urls')),  # ajout
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # URL pour la déconnexion
    path('supplier/', include('supplier.urls')),  # Exemple d'inclusion d'une autre application
    # ... d'autres chemins
    path('stockitem/', include('stockitem.urls')),
    path('order/', include('order.urls')), 
    path('department/', include('department.urls')),
    path('goodreceived/', include('goodreceived.urls')),
    path('stockrequest/', include('stockrequest.urls')),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),



   
]


