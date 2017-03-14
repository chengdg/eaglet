# -*- coding: utf-8 -*-


try:
	import settings
except ImportError:
	# from eaglet.core.exceptionutil import unicode_full_stack
	# print(unicode_full_stack())
	try:
		from django.conf import settings
	except:
		settings = None


def get_service_name():
	if settings and hasattr(settings, 'SERVICE_NAME'):
		return settings.SERVICE_NAME
	else:
		return 'unknown'


def get_settings():
	return settings
