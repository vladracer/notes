from django.conf.urls import patterns, url

from notesapp import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='notes')
)