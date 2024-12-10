from django.urls import path
from . import views

app_name = 'api'
urlpatterns = [
    #クラス
    path('item/', views.ItemView.as_view(), name='item')
]