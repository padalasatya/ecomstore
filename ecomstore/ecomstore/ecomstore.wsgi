import os
import sys	
sys.path.append('/home/satyapadala/public_html/py1.satyapadala.com/ecomstore/ecomstore/')
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
