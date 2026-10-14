from flask import Flask, Response

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1">
<meta name="theme-color" content="#0f172a">
<link rel="manifest" href="/manifest.json">
<title>MUS AWWAL BUSINESS CENTER - App</title>
<style>
*{margin:0;padding:0;box-sizing:border-box;font-family:sans-serif}
body{background:#f1f5f9;padding-bottom:80px}
.header{background:linear-gradient(135deg,#0f172a,#1e40af);color:white;padding:20px 15px;text-align:center;position:sticky;top:0;z-index:10}
.logo{font-size:28px;font-weight:900;letter-spacing:1px}
.tag{font-size:11px;opacity:0.8;margin-top:4px;letter-spacing:2px}
.card{background:white;margin:12px;border-radius:20px;padding:16px;box-shadow:0 4px 12px rgba(0,0,0,0.07)}
.hero{background:linear-gradient(135deg,#2563eb,#7c3aed);color:white;text-align:center;padding:25px 15px;border-radius:25px;margin:12px}
.btn-install{background:#facc15;color:#000;padding:12px 20px;border-radius:30px;font-weight:800;border:none;width:100%;margin-top:12px;font-size:15px}
.btn{display:inline-block;padding:10px 18px;border-radius:25px;text-decoration:none;font-weight:700;font-size:14px;margin:5px}
.btn-green{background:#25D366;color:white}
.btn-blue{background:#0f172a;color:white}
.service{display:flex;gap:12px;align-items:center;padding:12px 0;border-bottom:1px solid #f1f5f9}
.service:last-child{border:none}
.icon{width:48px;height:48px;border-radius:14px;display:flex;align-items:center;justify-content:center;font-size:22px}
.bottom-nav{position:fixed;bottom:0;left:0;right:
