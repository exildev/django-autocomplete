from distutils.core import setup
import os

# version (shape.function.path)
# python setup.py sdist upload
setup(
	name='django-autocomplete',
	version='0.0.1',
	packages=['django_autocomplete', ],
	url='https://github.com/exildev/django-autocomplete',
	author="Luis Miguel Morales Pajaro",
	author_email="luismiguel.mopa@gmail.com",
	licence="Creative Common",
	description="django autocomplete plugin",
	platform="Linux",
	zip_safe=False,
	include_package_data=True,
	package_data={'supra': ['templates/supra/*.html']},
)