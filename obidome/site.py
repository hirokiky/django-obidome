from django.conf import settings
from django.conf.urls import url

from obidome.conf.urls import include


urls = [url(r'^$', 'obidome.views.obidome')]
urls += [url(r'^%s/' % app_name,
             include(urls, wrapper, app_name=app_name))
         for urls, app_name, wrapper in settings.OBIDOME_URLS]
