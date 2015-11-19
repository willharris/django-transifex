from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.utils.functional import lazy

TRANSIFEX_USERNAME = getattr(settings, 'TRANSIFEX_USERNAME', None)
if TRANSIFEX_USERNAME is None:
    raise ImproperlyConfigured('You must set setting %r' % (
        'TRANSIFEX_USERNAME'
    ))

TRANSIFEX_PASSWORD = getattr(settings, 'TRANSIFEX_PASSWORD', None)
if TRANSIFEX_PASSWORD is None:
    raise ImproperlyConfigured('You must set setting %r' % (
        'TRANSIFEX_PASSWORD'
    ))


TRANSIFEX_HOST = getattr(settings, 'TRANSIFEX_HOST', 'https://www.transifex.net/')
SOURCE_LANGUAGE_CODE = getattr(settings, 'TRANSIFEX_SOURCE_LANGUAGE', settings.LANGUAGE_CODE)
RESOURCE_PREFIX = getattr(settings, 'TRANSIFEX_RESOURCE_PREFIX', '')
PROJECT_SLUG = getattr(settings, 'TRANSIFEX_PROJECT_SLUG', 'MyProject')


# Transifex might use different language codes to that used in the Django app.
# This dictionary will convert between them. The key is the transifex code,
# the value should be a string corresponding to the Django code
LANGUAGE_MAPPING = getattr(settings, 'TRANSIFEX_LANGUAGE_MAPPING', {})


def _get_locale_path():
    locale_path = getattr(settings, 'LOCALE_PATHS', tuple())
    return locale_path[0] if locale_path else './locale'


# Not strictly a setting, but this is a good place to keep it
LOCALE_PATH = getattr(settings, 'TRANSIFEX_LOCALE_PATH', _get_locale_path())
