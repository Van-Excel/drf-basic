from django.urls import path
from snippets import views


urlpatterns = [
    path('api/list',views.snippet_list, name= 'list' ),
    path('api/detail/<int:pk>', views.snippet_detail, name= 'detail'),
]
