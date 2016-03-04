from django.conf.urls import patterns, include, url
from djangoTest.views import hello,current_datetime,hours_ahead,extends_current_datetime,extends_hours_ahead

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djangoTest.views.home', name='home'),
    # url(r'^djangoTest/', include('djangoTest.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/$',hello),
    url(r'^time/$',current_datetime),
    url(r'^time/plus/(\d{1,2})/$',hours_ahead),
    url(r'^extends/$',extends_current_datetime),
    url(r'^extends/plus/(\d{1,2})/$',extends_hours_ahead),
)
