#!/usr/bin/env python3
"""
Simple HTTP Server for DeFi-Loops Calculator
Run this to avoid CORS issues when fetching live prices.

Usage:
    python server.py
    
Then open: http://localhost:8000
"""

import http.server
import socketserver
import webbrowser
from pathlib import Path

PORT = 8000

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Add CORS headers
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        super().end_headers()

if __name__ == "__main__":
    handler = MyHTTPRequestHandler
    
    with socketserver.TCPServer(("", PORT), handler) as httpd:
        print(f"🚀 DeFi-Loops Calculator Server Running!")
        print(f"📊 Open in browser: http://localhost:{PORT}")
        print(f"🔄 Live price fetching will work!")
        print(f"\n⏹️  Press Ctrl+C to stop\n")
        
        # Auto-open browser
        webbrowser.open(f'http://localhost:{PORT}')
        
        httpd.serve_forever()
