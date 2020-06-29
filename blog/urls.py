from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name = 'home'),
    path('workposts', views.post_list, name = 'post_list'),
    path('personal_post_list', views.personal_post_list, name = "personal_posts"),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/CV.html', views.cVAccess, name = "CV"),
]