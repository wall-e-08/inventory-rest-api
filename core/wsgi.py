"""
WSGI config for core project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application
from .settings import BASE_DIR

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

sys.path.append(os.path.join(BASE_DIR, "packages"))

application = get_wsgi_application()
