from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', "main.views.main_view", kwargs=None, name="main_view"),
)

from daylifenews import settings

if settings.SERVE_MEDIA:
    urlpatterns += patterns('',
        url(regex=r'^site-media/(?P<path>.*)$', view='django.views.static.serve', kwargs={'document_root': settings.MEDIA_ROOT}),
        url(regex='^media/(?P<path>.*)$',      view='django.views.static.serve', kwargs={'document_root': settings.ADMIN_MEDIA_ROOT}),
    )
