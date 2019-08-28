#
# Simple demo app
#
"""Simple Demo App"""
import os
from flask import Flask

MYAPP = Flask(__name__)

if 'HOSTNAME' in os.environ:
    CONTAINER_NAME = os.environ['HOSTNAME']
else:
    CONTAINER_NAME = os.uname()[1]

if 'BUILD_NUMBER' in os.environ:
    BUILD_NUMBER = os.environ['BUILD_NUMBER']
else:
    BUILD_NUMBER = "Unknown"

if 'BUILD_ENV' in os.environ:
    BUILD_ENV = os.environ['BUILD_ENV']
else:
    BUILD_ENV = "Unknown"

@MYAPP.route("/")
def index():
    """Return container name with build and environment information"""
    return CONTAINER_NAME + "  (BUILD: " + BUILD_NUMBER + " B.ENV: " + BUILD_ENV + ")"

@MYAPP.route("/healthz")
def status():
    """Return OK"""
    return "OK"

if __name__ == "__main__":
    # to use in local 'development' environment
    # when invoked directly
    os.environ['FLASK_ENV'] = 'development'
    MYAPP.run(host='0.0.0.0', port='8080', debug=True)

#
# END OF FILE
#
