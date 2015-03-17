from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.base import TemplateView
from django.http.response import HttpResponse
from django.contrib.auth.decorators import login_required
admin.autodiscover()

def XX(request):
    try:
        return XXX(request)
    except Exception as ee:
            print(ee,type(ee))
    return HttpResponse()
@login_required
def XXX(request):
    return HttpResponse('123S')
urlpatterns = patterns('',
                       url(r'^accounts/', include('allauth.urls')),
                       url(r'^$', TemplateView.as_view(template_name='index.html')),
#                        url(r'^accounts/profile/$', TemplateView.as_view(template_name='profile.html')),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^XX',XX),
)
