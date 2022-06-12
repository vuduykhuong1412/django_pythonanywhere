from django.urls import re_path

from . import views

app_name ="polls"


urlpatterns = [
    # # /polls/
    # re_path(r'^$', views.index, name='index'),
    # # /polls/5/
    # re_path(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # #/polls/5/results/
    # re_path(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # # /polls/5/vote/
    # re_path(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),

    re_path(r'^$', views.index, name='index'),
    re_path(r'^details/(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    re_path(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    re_path(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]