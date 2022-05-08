from django.utils.module_loading import import_string
from django.conf import settings


def get_password_validators():
    return [import_string(validator) for validator in settings.AUTH_PASSWORD_VALIDATORS]
