from django.contrib import admin
from django.urls import path,include
# import features
from features.views import search,getTrains,schedule,getTinfo,addR,addST,addRT,addT,cva,cn,cancel,book,book1,pnr
from .views import home
app_name='home'
urlpatterns = [
    path('user',home,name="home" ),
    
    path('search/', search, name='search'),
    path('search/trains', getTrains, name='get-trains'),
    path('schedule/', schedule, name='schedule'),
    path('schedule/trains', getTinfo, name='get-trains'),
    path('addR/', addR, name="addR"),
    path('addST/', addST, name='add-station'),
    path('addT/', addT, name='add-train'),
    path('addRT/',addRT),
    path('search/search/trains/cva/', cva,name='cva'),
    path('search/book1/', book1,name='book1'),
    path('search/book1/book/', book,name='book'),
    path('cancel/',cancel,name='cancel'),
    path('cancel/cancel/cn/',cn,name='cancl'),
    path('pnr/',pnr,name="pnr"),
    ]