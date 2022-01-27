
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
import django.utils.log

BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = '{{secret_key}}'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Словарь конфигурации логирования
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    # Форматы выдаваемых сообщений
    'formatters': {
        # Debug и выше, (уровень, время, сообщение)
        'base_format': {
            'format': '%(levelname)s %(asctime)s %(message)s'
        },
        # Warning и выше (включает путь к источнику события pathname)
        'warning_format': {
            'format': '%(levelname)s %(asctime)s %(pathname)s %(message)s'
        },
        # Error и Critical, файл errors.log (содержит стек ошибок exc_info)
        'error_format': {
            'format': '%(levelname)s %(asctime)s %(pathname)s %(exc_info)s %(message)s'
        },
        # general.log (время, уровень, название модуля)
        'general_format': {
            'format': '%(levelname)s %(asctime)s %(module)s'
        },
        # security.log (время, уровень, название модуля, сообщение)
        'security_format': {
            'format': '%(levelname)s %(asctime)s %(module)s %(message)s'
        }
    },
    # Фильтры. В консоль сообщения отправляются только при DEBUG = True, а на почту и в файл general.log — только при DEBUG = False.
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
    },
    # Обработчики сообщений, вывод по флагам, в консоль и/или log файл.
    'handlers': {
        # Debug и выше (если Debug = true)
        'base_console': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'base_format'
        },
        # Warning и выше (если Debug = true)
        'warning_console': {
            'level': 'WARNING',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'warning_format'
        },
        # Error и выше (если Debug = true)
        'error_console': {
            'level': 'ERROR',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'error_format'
        },
        # Info и выше
        'general_log_file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'general.log'),
            'formatter': 'general_format'
        },
        # Error и выше
        'error_log_file': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'errors.log'),
            'formatter': 'error_format'
        },
        # security.log
        'security_log_file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'security.log'),
            'formatter': 'security_format'
        },
        # Error и выше (если Debug = false)
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler',
            'formatter': 'warning_format'
        }
    },
    # Выделение сообщений логгера django
    'loggers': {
        # Вывод всех сообщений в консоль и запись в general.log от django
        'django': {
            'handlers': ['base_console', 'warning_console', 'error_console', 'general_log_file'],
            'propagate': True,
        },
        # Запись в errors.log и отправка по почте сообщений от django.request
        'django.request': {
            'handlers': ['error_log_file', 'mail_admins'],
            'propagate': False,
        },
        # Запись в errors.log и отправка по почте сообщений от django.server
        'django.server': {
            'handlers': ['error_log_file', 'mail_admins'],
            'propagate': False,
        },
        # Запись в errors.log сообщений от django.template
        'django.template': {
            'handlers': ['error_log_file'],
            'propagate': False,
        },
        # Запись в errors.log сообщений от django.db_backends
        'django.db_backends': {
            'handlers': ['error_log_file'],
            'propagate': False,
        },
        # Запись в security.log сообщений от django.security
        'django.security': {
            'handlers': ['security_log_file'],
            'propagate': False,
        },
    }

}

SITE_ID = 1

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',


    'django.contrib.sites',
    'django.contrib.flatpages',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware'
]

ROOT_URLCONF = 'logger.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'logger.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    BASE_DIR / "static"
]

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
