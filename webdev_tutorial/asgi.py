***REMOVED***
ASGI config for webdev_tutorial project.

It exposes the ASGI callable as a module-level variable named ``application``.

***REMOVED***
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
***REMOVED***

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'webdev_tutorial.settings')

application = get_asgi_application()
