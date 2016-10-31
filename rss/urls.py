from django.conf.urls import patterns, include, url

from django.contrib import admin
# from app.views import hello
from app.rss import views

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^weixin$', views.index),
    url(r'^rss/(.+)/$', views.feed),
    url(r'^rss_full/(.+)/$', views.full_text_feed)
)



