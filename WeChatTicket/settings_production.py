import os
CONFIGS = json.loads(open(os.path.join(BASE_DIR, 'configs_production.json')).read())
DEBUG = False

TEMPLATE_DEBUG = False

DATABASES = {
	'default':{
		'ENGINE': 'django.db.backends.mysql',
		'NAME': CONFIGS['DB_NAME'],
		'HOST': CONFIGS['DB_HOST'],
		'PORT': CONFIGS['DB_PORT'],
		'USER': CONFIGS['DB_USER'],
		'PASSWORD': CONFIGS['DB_PASSWORD'],
	}
}

ADMINS = (('Jingao Xu', 'xujingao13@gmail.com'),)

LOGGING = {
	'version': 1,
	'disable_existing_loggers': False,
	'handlers': {
		'console':{
			'level': 'INFO',
			'class': 'logging.StreamHandler',
		},
	},
	'loggers': {
		'django': {
			'handlers': ['console'],
			'propagate': True,
		},
	},
}

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

STATIC_ROOT = os.path.join(BASE_DIR, 'static').replace('\\', '/')
