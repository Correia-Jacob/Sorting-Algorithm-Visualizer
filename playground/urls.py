from django.urls import path
from . import views

#URLConf
urlpatterns = [
    path('', views.insertionsort),
    path('insertionsort/', views.insertionsort),
    path('displayInsertionsort/', views.displayInsertionsort),
    path('mergesort/', views.mergesort),
    path('displayMergesort/', views.displayMergesort),
    path('quicksort/', views.quicksort),
    path('displayQuicksort/', views.displayQuicksort),
    path('selectionsort/', views.selectionsort),
    path('displaySelectionsort/', views.displaySelectionsort)
]