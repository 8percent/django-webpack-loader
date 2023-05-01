import django

__author__ = 'Owais Lone'
__version__ = '0.7.1'

if django.VERSION < (3, 2):  # pragma: no cover
    default_app_config = 'webpack_loader.apps.WebpackLoaderConfig'
