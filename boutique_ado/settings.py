"""
Django settings for boutique_ado project.

Generated by 'django-admin startproject' using Django 3.2.25.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-^_40kijj^f*77%xy5b)mc%&gozs)d1ewck2f&uz@74zf(yw^y='

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Redirect URLs after login and logout
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',  # Required for django-allauth
    'allauth',  # django-allauth package
    'allauth.account',  # Account management (registration, login, etc.)
    'allauth.socialaccount',  # Social authentication (Google, Facebook, etc.)
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'boutique_ado.urls'

# Templating system (ensure 'context_processors.request' is in place for allauth)
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',  # Allauth requires this
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


# Authentication backends (django-allauth & default django backend)
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',  # Default authentication backend
    'allauth.account.auth_backends.AuthenticationBackend',  # Allauth authentication backend
)

# SITE_ID is required for django-allauth
SITE_ID = 1

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

ACCOUNT_AUTHENTICATED_REDIRECT_URL = '/'  # Redirect users after login
ACCOUNT_EMAIL_REQUIRED = True  # Make email required for registration
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'  # Email verification is mandatory
ACCOUNT_EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL = '/'  # Redirect users to home after email confirmation
ACCOUNT_USERNAME_REQUIRED = False  # Allow login with email instead of username
ACCOUNT_SIGNUP_EMAIL_ENTER_TWICE = True  # Require users to enter email twice to avoid typos
ACCOUNT_MINIMUM_USERNAME_LENGTH = 4  # Set minimum length for usernames (if you allow usernames)
LOGIN_REDIRECT_URL = '/'  # Temporary redirect URL after login


WSGI_APPLICATION = 'boutique_ado.wsgi.application'


# Database settings (SQLite for development)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation settings
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Localization settings
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Allauth settings (Optional, but useful)
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'  # For email verification after registration
ACCOUNT_AUTHENTICATED_REDIRECT_URL = '/'  # Redirect users after logging in

# The following settings are useful for customization
# You can change them as needed, these are just defaults.
ACCOUNT_USERNAME_REQUIRED = False  # Allow login via email only
ACCOUNT_SIGNUP_EMAIL_ENTER_TWICE = True  # Require email confirmation during signup
