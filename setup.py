#example structure

from setuptools import setup, find_packages

setup( 
	name='example_pkg',#name which will be used to install via pip
	version='1',#version number simple as that
	description='',
	long_description='',
	author='me',
	author_email='me@me.com',

	license='MIT',
	#which directories to search for imports. Importable dirs are marked by 
	packages=find_packages(include=["example_pkg","example_pkg.*"]),
	#packages=find_packages()#also possible but may include unwanted dir such as tests
	zip_safe=False,
	entry_points={
        'console_scripts': ['testImportRunner=example_pkg.main:run']
    },
	setup_requires=['pytest-runner'],
    tests_require=['pytest'],
)