from blog import views
from django.urls import path
app_name='blog'

urlpatterns=[
    path('',views.index,name='index'),
    path('list',views.listView,name='list'),
    path('about',views.aboutView,name='about'),
    path('posts/<int:pk>/',views.detail,name='detail'),
    path('archives/<int:year>/<int:month>/',views.archive,name='archive'),
    path('categories/<int:pk>/',views.category,name='category'),
    path('tags/<int:pk>/',views.tag,name='tag'),
]