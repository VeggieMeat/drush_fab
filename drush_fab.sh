#!/bin/bash
FABFILE=/usr/local/bin/drush_fab/fabfile.py

HOST=$1
USER=$2
DIR=$3
URI=$4

fab -f $FABFILE -H $HOST cron:user=$USER,dir=$DIR,uri=$URI || exit 1
