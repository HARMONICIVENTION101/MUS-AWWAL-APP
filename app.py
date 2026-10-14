from flask import Flask, Response

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="theme-color" content="#0f172a">
<link rel="manifest" href="/manifest.json">
<title>MUS AWWAL BUSINESS CENTER - App</title>
<style>
*{margin:0;padding:0;box-sizing:border-box;font-family:sans-serif}
body{background:#f1f5f9;padding-bottom:80px}
.header{background:linear-gradient(135deg,#0f172a,#2563eb);color:white;padding:22px;text-align:center}
.logo{font-size:28px;font-weight:900;letter-spacing:1px}
.tag{font-size:11px;opacity:0.8;margin-top:4px;letter-spacing:2px}
.card{background:white;margin:12px;border-radius:16px;padding:18px;box-shadow:0 2px 8px rgba(0,0,0,0.06)}
.hero{background:linear-gradient(135deg,#2563eb,#0f172a);color:white}
.btn-install{background:#facc15;color:#000;padding:12px 20px;border-radius:12px;border:none;font-weight:800;width:100%;margin-top:12px;font-size:16px}
.btn{display:inline-block;padding:10px 18px;border-radius:10px;text-decoration:none;font-weight:700;margin:4px;font-size:14px}
.btn-green{background:#25D366;color:white}
.btn-blue{background:#0f172a;color:white}
.service{display:flex;gap:12px;align-items:center;padding:12px 0;border-bottom:1px solid #e2e8f0}
.service:last-child{border:none}
.icon{width:48px;height:48px;border-radius:14px;display:flex;align-items:center;justify-content:center;color:white;font-size:22px;flex-shrink:0}
.bottom-nav{position:fixed;bottom:0;left:0;right:0;background:white;border-top:1px solid #e2e8f0;display:flex;justify-content:space-around;padding:8px 0;z-index:99}
.nav-item{text-align:center;text-decoration:none;color:#64748b;font-size:10px;font-weight:700}
.nav-item span{display:block;font-size:22px}
.nav-active{color:#2563eb}
</style>
</head>
<body>
<div class="header">
<div class="logo">MUS AWWAL</div>
<div class="tag">BUSINESS CENTER</div>
<div style="margin-top:8px;font-size:13px;opacity:0.9">CAC REG • FAST • TRUSTED • NATIONWIDE</div>
</div>

<div class="card hero">
<h2>Welcome! 👋</h2>
<p style="margin:10px 0;font-size:14px;line-height:1.5">We register your business, secure your brand, and help you grow online.</p>
<button class="btn-install" id="installBtn" style="display:none">📲 Install App to Phone</button>
<p style="font-size:11px;margin-top:8px;opacity:0.8">Install like WhatsApp - works offline!</p>
</div>

<div class="card">
<h3 style="margin-bottom:12px">🚀 Our Services</h3>
<div class="service"><div class="icon" style="background:#2563eb">🏢</div><div><b>CAC Registration</b><br><small style="color:#64748b">Business Name, Ltd, NGO in 3-7 days</small></div></div>
<div class="service"><div class="icon" style="background:#16a34a">🎨</div><div><b>Logo & Design</b><br><small style="color:#64748b">Professional branding</small></div></div>
<div class="service"><div class="icon" style="background:#dc2626">🌐</div><div><b>Website Development</b><br><small style="color:#64748b">Business website + App</small></div></div>
<div class="service"><div class="icon" style="background:#7c3aed">📈</div><div><b>Digital Marketing</b><br><small style="color:#64748b">Get customers online</small></div></div>
</div>

<div class="card" style="text-align:center">
<h3>Chat With Us</h3>
<p style="color:#64748b;font-size:13px;margin:8px 0">Fast response on WhatsApp</p>
<a class="btn btn-green" href="https://wa.me/2347037530754">WhatsApp Us</a>
<a class="btn btn-blue" href="tel:+2347037530754">Call Now</a>
</div>

<div class="bottom-nav">
<a class="nav-item nav-active" href="/"><span>🏠</span>HOME</a>
<a class="nav-item" href="https://wa.me/2347037530754"><span>💬</span>CHAT</a>
<a class="nav-item" href="tel:+2347037530754"><span>📞</span>CALL</a>
<a class="nav-item" href="#"><span>👤</span>PROFILE</a>
</div>

<script>
let deferredPrompt;
const installBtn = document.getElementById('installBtn');
window.addEventListener('beforeinstallprompt', (e) => {
  e.preventDefault();
  deferredPrompt = e;
  installBtn.style.display = 'block';
});
installBtn.addEventListener('click', () => {
  if (deferredPrompt) {
    deferredPrompt.prompt();
    deferredPrompt.userChoice.then(() => { deferredPrompt = null; installBtn.style.display='none'; });
  }
});
if ('serviceWorker' in navigator) {
  navigator.serviceWorker.register('/sw.js');
}
</script>
</body>
</html>
"""

MANIFEST = """{
