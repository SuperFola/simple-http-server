#!/usr/bin/env python

import SimpleHTTPServer
import SocketServer
import urlparse


PORT = 8080
f = open('./logs', 'w+')

class RequestHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def __init__(self, request, client_addr, server):
        SimpleHTTPServer.SimpleHTTPRequestHandler.__init__(self, request, client_addr, server)

    def block(self):
        print >> f, "rejected"
        self.send_response(403)
        self.end_headers()
        self.wfile.write("No.")

    def do_GET(self):
        parsed = urlparse.urlparse(self.path)
        print >> f, parsed
        forbidden = (
            "?", "&", ".php", "wp-content", ".git", "vendor", "console",
            "http", "owa",
        )
        if any(s in parsed for s in forbidden):
            self.block()
        else:
            SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)

    def do_POST(self):
        self.block()


handler = RequestHandler
httpd = SocketServer.TCPServer(('', PORT), handler)

print >> f, "serving at port", PORT
httpd.serve_forever()