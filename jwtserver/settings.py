"""
Django settings for jwtserver project.

Generated by 'django-admin startproject' using Django 1.11.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""
import datetime
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'u(gt!zcb2oqa*yf4s##g2u_-7)v9r0g3m+1^+2_!&f+8xuwaeq'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'user',
    'rest_framework',
    'django_filters',

]

MIDDLEWARE = [
    'common.middlemare.NotifySalesTokenMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'jwtserver.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'yaozc/templates'), os.path.join(BASE_DIR, 'yaozc/templates-h5')],
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

WSGI_APPLICATION = 'jwtserver.wsgi.application'

AUTH_USER_MODEL = 'user.AgentOrSaleManOrOperate'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'jwt1',
        'USER': 'root',
        'PASSWORD': '4546',
        'HOST': 'localhost',
        'PORT': '3306',
        "TEST": {
            "NAME": "jwt_test",
            "CHARSET": "utf8",
            "COLLATION": "utf8_general_ci",
        }
    }
}



# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS':
        'common.pagination.StandardPagination',
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    ),
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
    )
}

# 设置邮箱和用户名和手机号均可登录
AUTHENTICATION_BACKENDS = (
    'user.views.CustomBackend',
)

#jwt认证token过期时间
JWT_AUTH = {
    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=2),
    'JWT_AUTH_HEADER_PREFIX': 'JWT',
    # 'JWT_PAYLOAD_GET_USERNAME_HANDLER': 'common.middleware.jwt_get_username_from_payload_handlers',
    'JWT_ALGORITHM': 'RS256',
    'JWT_PRIVATE_KEY':"""-----BEGIN RSA PRIVATE KEY-----
MIIEpAIBAAKCAQEArJjja2lkDpXBPqbHydTWdKgedaNmBLyc6gJwx6tAOVaP7gZD
ms1KjaS0Fqyl5Z/h+8ylNaNiGU/dM7r7npSYjxBxE9UCCek73kcM6CVCchmiW7JM
VZU/RZZqrJzP6tnTV+A/G8zyteNsTWlXYv508vedqDIHyTQ6qE0gA6roQPydWcYa
xipX54wUpZ/mBK9wWQaxLzIK8fsLqug/71myGafmlU2zBwFSSv+7TMNVjvh2CjFf
++nuXno+01Bch0MMqL4ucMIBMQJXwL/DbcCy40U9bHbQwwWtViUAftnhY5o7Sp8a
qzIgrmcyLrJiqDkZnjk2NI9ny3oWVv1ZnkSMYQIDAQABAoIBAQCqg5kaAtLQ/e4e
YVK7+UOtmHIPMlCVmWlEXwjgmjUm8HfdZd7gTrS63t70D7kN9DikNPd62GEQNLCK
bM4tSwy1Oj8corIS7JMy8+qyZi0Q4HZgNPPpETujGgllYr6efHipNmfipUWboITc
rZehu1X6u9rL0jGS+8B/iUJ5nR07JTbeyFNOZGnObFz3ZHHOnqgctIw0uxTvRypl
au/vq00JuWnj2MRYUMA0p66jqbirl0ebSRwI1j26JeH/KT9S/Cl/Fv/5RjyQUuEc
wmbIIaI1ugpKFeBwELN8/6H39D1AID73BOsb11B2t+SNxW0WXk365X6VLU27XwDL
9To7kduBAoGBANwrM935R4qJ5KpxfXPDwwBbTml71dWP+cMCuJSVBxD/uTJdhfAE
R06sunQq7h8S6Xh+i6r6zT5Mu3rvJicqfA/6/otgN5nJuZAAnVFETapayCX+cOom
KPTBMysKBoE05CW1AgwB/bGtQEr8OID1ToUDuCQm/9yLDiYvp+QQCwM5AoGBAMiv
u6Bvo1NIEqW6EFUoEUTrcTd+EHPwsYLPDkj6IpAQVJ8dZbArgMBjZbXsYehTjgxx
DOotQKBpCIVaIP5xEBnSblcf66etEK0ugYgMdSa6TpPf7Tv4U9ad7nIIbKX3stJt
GiiWdCVPtPZPc1CTR48ukoZwC5MX8kydtLlYoAppAoGBALuV26U+pOO2xSsrcvXV
TynYoaBiMDi7aNPsV5PQvaqQFxyAboOnQZIYvOwJP8Ud+en998X/1itEeWAurlUk
b3u2IHZjzjurkfzNaTw6c+m3W1xzw4TcanzOt2fuLMidZd1ysYHFmH9v252H9CR7
3SCboKK8z7b6i12hsOwxdxCRAoGAHLLkxgCw/ovj/sco5sSgE5cHzcO9XpchC2/I
vy7mGmv7bfWqQRM3ikusk+OF7M9mFOlly2dFQqtCiK9m4HwSrV6mYNczv/rD08A+
zdHaPvuNmSAAsP7GHn7fRndl8iYF8ImhoARD/8HyQvcBqpglN5iVY5xKS3K1N7el
zIub92ECgYA24OeTQoVV9Sdx+pgKc7WJnpwcFTsZPfXEbVGQ5uWSeenHy5AqWHF1
KYTcTYAfXUJJEtJO8tm3SR7GBMYyGMPlsxi0iiiNbOun37395LBgxVzpiHVKI3NY
9KAD/frQ88sjkF6yf7ZaLWYtt4eTnxJyB/qJRuczaQlhjdzsXCbOIw==
-----END RSA PRIVATE KEY-----
""",
    'JWT_PUBLIC_KEY': """ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCsmONraWQOlcE+psfJ1NZ0qB51o2YEvJzqAnDHq0A5Vo/uBkOazUqNpLQWrKXln+H7zKU1o2IZT90zuvuelJiPEHET1QIJ6TveRwzoJUJyGaJbskxVlT9FlmqsnM/q2dNX4D8bzPK142xNaVdi/nTy952oMgfJNDqoTSADquhA/J1
ZxhrGKlfnjBSln+YEr3BZBrEvMgrx+wuq6D/vWbIZp+aVTbMHAVJK/7tMw1WO+HYKMV/76e5eej7TUFyHQwyovi5wwgExAlfAv8NtwLLjRT1sdtDDBa1WJQB+2eFjmjtKnxqrMiCuZzIusmKoORmeOTY0j2fLehZW/VmeRIxh 563672373@qq.com""",
}

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'
CELERY_TIMEZONE = TIME_ZONE

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
