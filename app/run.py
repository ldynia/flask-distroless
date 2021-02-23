"""
Run this file with uwsgi
$ cd /srv/www/htdocs/config/services
$ uwsgi --ini app.uwsgi.development.ini --http-socket /var/run/app.sock
"""
import os

from app import create_app

app = create_app()

from app.modules.demo.hello import *

if __name__ == "__main__":
    PORT = os.getenv('PORT', 80)
    HOST = os.getenv('HOST', '0.0.0.0')

    app.run(host=HOST, port=PORT, threaded=True)
