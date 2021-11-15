from django.urls import path
from . import views

urlpatterns=[
    
    path('prestamos',views.prestamos),
    path('prestamos/<int:prestamo_id>',views.prestamodetalle)
]