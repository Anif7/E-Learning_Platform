from .base import *

DEBUG = False

SECRET_KEY = 'y3bb5m11j6fm&j%-d87t=fg2bw+d&c00#))s^zk!#!w890z2(b'

ADMINS = (
    ('Antonio M', 'email@mydomain.com'),
)

ALLOWED_HOSTS = ['*'] 

DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.postgresql',
       'NAME': 'educa',
       'USER': 'educa',
       'PASSWORD': 'Anif@2243',
       'HOST':'localhost',
       'PORT':'5432',
   }
}

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True


