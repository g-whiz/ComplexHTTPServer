#!/bin/env python

try:
    # Python3
    import http.server as SimpleHTTPServer
    import http.server as BaseHTTPServer
    import socketserver as SocketServer
except ImportError:
    # Python 2
    import SimpleHTTPServer
    import BaseHTTPServer
    import SocketServer

import sys
import os
import argparse

# The absolute path of the directoy for this file:
_ROOT = os.path.abspath(os.path.dirname(__file__))

class ThreadingSimpleServer(SocketServer.ThreadingMixIn,BaseHTTPServer.HTTPServer):
    pass

parser = argparse.ArgumentParser('ComplexHTTPServer: now with more threads!')
parser.add_argument('port', metavar='PORT', type=int, default=8000,
                    help='The port to serve on.')
parser.add_argument('--host', dest='ip', type=str, default='127.0.0.1',
                    help='The IP address to serve on.')
config = parser.parse_args()

server = ThreadingSimpleServer((config.ip, config.port), SimpleHTTPServer.SimpleHTTPRequestHandler)
print("Serving HTTP on {}:{}".format(config.ip, config.port))

try:
    while 1:
        sys.stdout.flush()
        server.handle_request()
except KeyboardInterrupt:
    print("Finished")
