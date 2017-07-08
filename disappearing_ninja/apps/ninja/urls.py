from django.conf.urls import url
from apps.ninja import views
urlpatterns = (
    url(r'^', views.all, name='all'),
    url(r'^(?P<color>\w+)/$', views.ninja, name='ninja'),
)
