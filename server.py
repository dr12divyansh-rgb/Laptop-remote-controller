from http.server import BaseHTTPRequestHandler, HTTPServer
import os

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):

        print("Request received:", self.path)

        if "/notepad" in self.path:
            os.system("notepad")

        elif "/chrome" in self.path:
            os.system("start chrome")

        elif "/shutdown" in self.path:
            os.system("shutdown /s /t 5")

        elif "/restart" in self.path:
            os.system("shutdown /r /t 5")

        elif "/lock" in self.path:
            os.system("rundll32 user32.dll,LockWorkStation")

        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"OK")

server = HTTPServer(("0.0.0.0", 12345), Handler)

print("HTTP Server started on port 12345...")
server.serve_forever()
