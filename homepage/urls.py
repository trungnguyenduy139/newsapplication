from django.conf.urls import url
from . import views

urlpatterns = [
    # /homepage
    url(r'^$', views.index, name='index'),

    # /homepage/555/
    url(r'^(?P<post_id>[0-9]+)$', views.detail, name='detail'),

]
