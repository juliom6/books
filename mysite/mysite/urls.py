from django.conf.urls import patterns, include, url
from mysite.views import hola, inicio, fecha_actual, fecha_horas_adelante

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
	('^$', inicio),
	('^holas/$', hola),
	('^fecha/$', fecha_actual),
	(r'^fecha/mas/(\d{1,2})/$', fecha_horas_adelante),
)
