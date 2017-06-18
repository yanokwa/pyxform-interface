from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views
#from django.conf import settings
#from django.views.generic.simple import direct_to_template
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    url(r'^json_workbook/', views.json_workbook),
    url(r'^$', views.index),
    url(r'^downloads/(?P<path>.*)$', views.serve_file),
]

urlpatterns += staticfiles_urlpatterns()
