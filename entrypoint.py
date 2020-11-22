#!/usr/bin/env python

import SimpleHTTPServer
import SocketServer
import urlparse


PORT = 8080


class RequestHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def __init__(self, request, client_addr, server):
        super().__init__(request, client_addr, server)

    def block(self):
        self.send_response(403)
        self.end_headers()
        self.wfile.write("No.")

    def do_HEAD(self):
        super(RequestHandler, self).do_HEAD()

    def do_GET(self):
        parsed = urlparse.urlparse(self.path)
        if "?" in parsed or "&" in parsed:
            self.block()
        else:
            super(RequestHandler, self).do_GET()

    def do_POST(self):
        self.block()


handler = SimpleHTTPServer.SimpleHTTPRequestHandler
httpd = SocketServer.TCPServer(('', PORT), handler)

print "serving at port", PORT
httpd.serve_forever()