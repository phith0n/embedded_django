import os
import sys
import netius.servers
from django.conf.urls import url
from django.shortcuts import render
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", __name__)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DEBUG = True
SECRET_KEY = '__secret_key__'

ROOT_URLCONF = __name__
TEMPLATES = [{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [os.path.join(BASE_DIR, 'templates')]
}]


def home(request):
    return render(request, 'hello.html', context=dict(
        title='Hello world!',
        author='phith0n'
    ))


urlpatterns = [
    url(r'^$', home),
]

if DEBUG:
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
else:
    application = get_wsgi_application()
    server = netius.servers.WSGIServer(app=application)
    server.serve(port=8000)
