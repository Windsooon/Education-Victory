import os
from pathlib import Path

import dj_database_url

BASE_DIR = Path(__file__).resolve().parent.parent
DEFAULT_DIR = Path(__file__).resolve().parent
STATIC_DIR = Path(__file__).resolve().parent.parent.parent

ENVIRONMENT = os.getenv('ENVIRONMENT')

if ENVIRONMENT in ('LOCAL', 'TEST'):
    DEBUG = True
    ROOT = 'http://127.0.0.1:8000'
    ALLOWED_HOSTS = ['localhost', '127.0.0.1']
    SECRET_KEY = 'django-insecure-@s=_aoq!k!h-@b^%t!+zoxo4fs@e+ccr^lld4fd9+3oxdg^!^!'
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
    if ENVIRONMENT == 'TEST':
        DATABASES = {
            "default": {
                "ENGINE": "django.db.backends.sqlite3",
                "NAME": "mydatabase",
            }
        }
    else:
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.postgresql',
                'NAME': 'postgres',
                'USER': 'postgres',
                'PASSWORD': 'test',
                'HOST': 'localhost',
                'PORT': '5432',
            }
        }
    STATIC_URL = 'static/'
    STATICFILES_DIRS = [
        STATIC_DIR / "static",
    ]
elif ENVIRONMENT in ('STAGE', 'PRODUCTION'):
    if ENVIRONMENT == 'STAGE':
        DEBUG = True
        SECRET_KEY = 'django-insecure-@s=_aoq!k!h-@b^%t!+zoxo4fs@e+ccr^lld4fd9+3oxdg^!^!'
    else:
        DEBUG = False
        SECRET_KEY = os.getenv('SECRET_KEY')
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
    ROOT = os.getenv('ROOT')
    STATIC_ROOT = os.path.join(STATIC_DIR, 'static')
    ALLOWED_HOSTS = [os.getenv('HOST')]
    CSRF_TRUSTED_ORIGINS = [os.getenv('CSRF')]

    DATABASES = {
        'default': dj_database_url.parse(
            os.getenv('DATABASE_URL'),
            conn_max_age=600,
            conn_health_checks=True,
            )
    }
    STATIC_URL = os.getenv('STATIC_CDN')


OPENAI_SECRET_KEY = os.getenv('OPENAI_SECRET_KEY')

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    'django_extensions',
    'common.apps.CommonConfig',
    'problem.apps.ProblemConfig',
    'question.apps.QuestionConfig',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.openid',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.github',
    'rest_framework',
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

AUTH_USER_MODEL = 'common.User'

ROOT_URLCONF = 'EX.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(DEFAULT_DIR, 'templates')], # import the templates folder
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'EX.wsgi.application'

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

AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',
    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

SITE_ID = 1

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        },
        'OAUTH_PKCE_ENABLED': True,
    },
    'github': {
        'SCOPE': [
            'user',
            'repo',
            'read:org',
        ],
    }
}

# Email
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = True

# Enhance
ACCOUNT_USERNAME_REQUIRED = True
ACCOUNT_LOGOUT_ON_PASSWORD_CHANGE = True

# Other
LOGIN_REDIRECT_URL = 'home'
ACCOUNT_LOGOUT_REDIRECT_URL = 'home'
SOCIALACCOUNT_LOGIN_ON_GET = True
ACCOUNT_LOGOUT_ON_GET = True
