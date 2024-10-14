import http.server
import socketserver
import os
from datetime import datetime
import mimetypes

PORT = 8000
REQUEST_DIR = "request"
IMAGE_DIR = "images"

class CustomHTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        timestamp = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        os.makedirs(REQUEST_DIR, exist_ok=True)
        os.makedirs(IMAGE_DIR, exist_ok=True)

        # 保存请求数据
        request_filename = os.path.join(REQUEST_DIR, f"{timestamp}.bin")
        with open(request_filename, 'wb') as file:
            file.write(post_data)

        # 解析和保存图片
        boundary = self.headers.get_boundary().encode()
        parts = post_data.split(boundary)
        for part in parts:
            if b'Content-Disposition: form-data; name="image"' in part:
                headers, image_data = part.split(b'\r\n\r\n', 1)
                image_data = image_data.rstrip(b'\r\n--')
                image_filename = os.path.join(IMAGE_DIR, f"{timestamp}.jpg")
                with open(image_filename, 'wb') as img_file:
                    img_file.write(image_data)
                print(f"Image saved to {image_filename}")

        # 发送响应
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.end_headers()
        self.wfile.write(b"<html><head><title>Socket Server</title></head><body>I've got your message</body></html>")

Handler = CustomHTTPRequestHandler
httpd = socketserver.TCPServer(("", PORT), Handler)

print(f"Serving at port {PORT}")
httpd.serve_forever()
