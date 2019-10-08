from django.conf.urls import url
from . import views

urlpatterns = [
    url('^$',views.welcome,name='welcome'),
    url('^today/$',views.news_of_day,name='newsToday'),
    url('^archives/(\d{}-\d{}-\d{})/$',views.past_days_news,name='pastNews')
]