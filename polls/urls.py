from django.conf.urls import url

from . import views

urlpatterns = [
    # /polls/
    url(r'^$', views.index, name='index'),
    # /polls/:question_id
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # /polls/:question_id/results/
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # /polls/:question_id/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
