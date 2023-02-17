from http.server import BaseHTTPRequestHandler, HTTPServer, ThreadingHTTPServer
import time
import json
from socketserver import ThreadingMixIn
import threading
hostName = '0.0.0.0'
serverPort = 80
class Handler(BaseHTTPRequestHandler):
 def do_GET(self):
  if self.path == '/':
    self.send_response(200)
    self.send_header("content-type", "text/html")
    self.end_headers()
    content = open("index.html", "rb").read()
    self.wfile.write(content)
  else:
    self.send_response(404)
    return
class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    if __name__ == "__main__":
        webServer = ThreadingHTTPServer((hostName, serverPort), Handler)
        print ("Server started http://%s:%s" % (hostName, serverPort))
        try:
            webServer.serve_forever()
        except KeyboardInterrupt:
            pass
        webServer.server_close()
        print("Server stopped.")
    