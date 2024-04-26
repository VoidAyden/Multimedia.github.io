from http.server import HTTPServer, BaseHTTPRequestHandler

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            with open('templates/index.html', 'r') as f:
                content = f.read()
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(bytes(content, 'utf8'))
        except:
            self.send_response(404)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'404: File not found')

httpd = HTTPServer(('', 8000), MyHandler)
httpd.serve_forever()
import http.server, ssl

# Set the server address and port number
server_address = ('localhost', 4443)

# Set the paths to the SSL certificate and key files
certfile = 'cert.pem'
keyfile = 'key.pem'

# Create an SSL wrapper for the server
httpd = http.server.HTTPServer(server_address, http.server.SimpleHTTPRequestHandler)
httpd.socket = ssl.wrap_socket(httpd.socket, server_side=True, certfile=certfile, keyfile=keyfile)

# Start the server
print(f'Serving HTTPS on {server_address[0]}:{server_address[1]}...')
httpd.serve_forever() 
