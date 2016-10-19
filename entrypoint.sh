#!/bin/bash
set -e

sysctl -w net.core.somaxconn=65535

python manage.py collectstatic --noinput


exec "$@"
