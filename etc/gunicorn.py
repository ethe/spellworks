# coding: utf-8

import gevent.monkey
gevent.monkey.patch_all()
import multiprocessing

bind = '127.0.0.1:8089'
max_requests = 10000
keepalive = 5

workers = multiprocessing.cpu_count() * 2 + 1
worker_class = 'gunicorn.workers.ggevent.GeventWorker'

loglevel = 'info'
errorlog = '-'

x_forwarded_for_header = 'X-FORWARDED-FOR'

secure_scheme_headers = {
    'X-SCHEME': 'https',
}
