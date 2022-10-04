from django.urls import path
from directory.views import index,insert,amend,remove
urlpatterns = [
    path('',index,name='index'),
    path('insert',insert,name='insert'),
    path('amend/<int:id>/',amend,name='amend'),
    path('remove/<int:id>/',remove,name='remove')
]
