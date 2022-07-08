#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
from http.server import HTTPServer, BaseHTTPRequestHandler

class HealthCheck(BaseHTTPRequestHandler):

    def do_GET(self):
        if check():
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"healthy\n")
        else:
            self.send_error(404)

    def do_HEAD(self):
        self.do_GET()

def check():
    status = os.system('systemctl is-active --quiet rsyslog')
    print(status)
    if(status == 0):
        return True
    else:
        return False



def main():
    server = HTTPServer(('', 8080), HealthCheck)
    server.serve_forever()


if __name__ == "__main__":
    main()
