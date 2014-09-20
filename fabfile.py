from fabric.api import *
from fabric.contrib.files import exists
import time

env.user = user
env.shell = '/bin/bash -c'

def cron(dir, uri):
  print "===> Running cron"
  with prefix("cd %s" %(dir)):
    run("drush --uri=%s cron --debug" %(uri))
