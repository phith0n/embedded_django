import os
import sys
import importlib
from django.urls import include, path
from django.shortcuts import render
from django.core.wsgi import get_wsgi_application
from django.apps import AppConfig


os.environ.setdefault("DJANGO_SETTINGS_MODULE", __name__)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DEBUG = True
SECRET_KEY = '__secret_key__'
ALLOWED_HOSTS = ['*']

ROOT_URLCONF = __name__
TEMPLATES = [{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [os.path.join(BASE_DIR, 'templates')]
}]
MIDDLEWARE = [
    'django.middleware.common.CommonMiddleware',
]
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'WARNING'),
        },
    },
}


def home(request):
    return render(request, 'hello.html', context=dict(
        title='Hello world!',
        author='phith0n'
    ))


class MainConfig(AppConfig):
    name = __name__
    default_auto_field = 'django.db.models.BigAutoField'

    def ready(self):
        self.models_module = importlib.import_module('app')


INSTALLED_APPS = [
    MainConfig('app', importlib.import_module(__name__)),
]
urlpatterns = [
    path('', home),
]

if DEBUG:
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
else:
    import netius.servers
    application = get_wsgi_application()
    server = netius.servers.WSGIServer(app=application)
    server.serve(port=8000)
