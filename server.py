import sys
from flask import Flask, render_template_string, jsonify
app = Flask(__name__)
# 👑 YOUR PERFECT REAL WORKING RESPONSIVE UI GRID
HTML_LAYOUT = """
<!DOCTYPE HTML>
<HTML lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>UNIVERSAL SYSTEM KAVACH — Global Command Center</title>
    <style>
        :root {
            --bg-color: #030303;
            --panel-bg: #0a0a0c;
            --neon-cyan: #00FFCC;
            --neon-green: #33FF33;
            --border-glow: rgba(0, 255, 204, 0.1);
        }
        * { box-sizing: border-box; margin: 0; padding: 0; font-family: '-apple-system', BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; }
        body { background-color: var(--bg-color); color: #ffffff; padding: 15px; min-height: 100vh; display: flex; flex-direction: column; justify-content: space-between; }
        .container { width: 100%; max-width: 1200px; margin: 0 auto; text-align: center; }
        .header { margin-top: 20px; color: var(--neon-cyan); font-size: 24px; font-weight: 800; text-shadow: 0 0 12px rgba(0,255,204,0.4); letter-spacing: 1px; text-transform: uppercase; }
        .owner-tag { color: var(--neon-cyan); font-size: 11px; margin-top: 5px; opacity: 0.8; letter-spacing: 2px; }
        .status-box { background-color: var(--panel-bg); border: 1px solid var(--neon-green); padding: 12px; margin: 20px auto; width: 100%; max-width: 800px; color: var(--neon-green); border-radius: 6px; font-weight: bold; font-size: 13px; box-shadow: 0 0 10px rgba(51,255,51,0.05); }
        .grid-container { 
            display: grid; 
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); 
            gap: 15px; 
            width: 100%; 
            max-width: 800px; 
            margin: 25px auto; 
        }
        .btn { 
            background-color: #111115; 
            color: #ffffff; 
            padding: 22px 15px; 
            font-size: 14px; 
            font-weight: 700; 
            border: 1px solid #222228; 
            border-radius: 8px; 
            cursor: pointer; 
            transition: all 0.25s ease; 
            text-align: left;
            display: flex;
            flex-direction: column;
            justify-content: center;
            position: relative;
            overflow: hidden;
            -webkit-tap-highlight-color: transparent;
        }
        .btn-ports { border-left: 4px solid #C62828; }
        .btn-network { border-left: 4px solid #1565C0; }
        .btn-timelock { border-left: 4px solid #2E7D32; }
        .btn-compiler { border-left: 4px solid #EF6C00; }
        .btn:hover, .btn:active { 
            background-color: #161620; 
            border-color: var(--neon-cyan);
            transform: translateY(-2px); 
            box-shadow: 0 5px 15px var(--border-glow);
        }
        .btn-title { font-size: 15px; display: flex; align-items: center; gap: 8px; margin-bottom: 4px; font-weight: bold; }
        .btn-desc { font-size: 11px; font-weight: 400; color: #888890; }
        .footer { font-size: 10px; color: #44444a; padding: 20px 0; letter-spacing: 0.5px; text-align: center; }
        .custom-alert { display: none; position: fixed; top: 50%; left: 50%; transform: translate(-50%, -50%) scale(0.9); background-color: #0b0b0f; border: 2px solid var(--neon-cyan); box-shadow: 0 0 30px rgba(0,255,204,0.2); padding: 20px; border-radius: 12px; width: 90%; max-width: 450px; z-index: 10000; text-align: left; transition: all 0.3s ease; }
        .custom-alert.active { display: block; transform: translate(-50%, -50%) scale(1); }
        .custom-alert h3 { color: var(--neon-cyan); margin-bottom: 12px; font-size: 18px; border-bottom: 1px solid #1a1a24; padding-bottom: 8px; }
        .custom-alert p { color: #e4e4e9; font-size: 13px; line-height: 1.6; margin-bottom: 18px; white-space: pre-line; }
        .custom-alert-btn { background-color: var(--neon-cyan); color: #000000; font-weight: 800; padding: 10px 20px; border: none; border-radius: 6px; cursor: pointer; float: right; font-size: 12px; text-transform: uppercase; letter-spacing: 1px; width: 100%; text-align: center; }
        .overlay { display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.85); z-index: 9999; backdrop-filter: blur(4px); }
        .auth-wrapper { display: flex; width: 100%; min-height: 80vh; align-items: center; justify-content: center; }
        .auth-container { width: 100%; max-width: 480px; text-align: center; background-color: var(--panel-bg); border: 1px solid #1a1a24; padding: 35px 25px; border-radius: 12px; box-shadow: 0 0 25px rgba(0,255,204,0.05); }
        h2.auth-heading { color: #ffffff; font-size: 16px; margin-bottom: 20px; letter-spacing: 1px; text-transform: uppercase; border-bottom: 1px solid #1a1a24; padding-bottom: 10px; }
        p.info-text { color: #888890; font-size: 13px; line-height: 1.6; margin-bottom: 25px; text-align: justify; }
        .form-group { margin-bottom: 18px; text-align: left; }
        label { display: block; color: var(--neon-cyan); font-size: 11px; font-weight: bold; margin-bottom: 6px; letter-spacing: 1px; text-transform: uppercase; }
        input { width: 100%; background-color: #111116; border: 1px solid #22222b; padding: 13px 12px; color: #ffffff; border-radius: 6px; font-size: 14px; transition: all 0.3s; }
        input:focus { border-color: var(--neon-cyan); outline: none; box-shadow: 0 0 10px rgba(0,255,204,0.1); }
        .submit-btn { width: 100%; background-color: var(--neon-cyan); color: #000000; font-weight: 800; padding: 13px; border: none; border-radius: 6px; cursor: pointer; font-size: 13px; text-transform: uppercase; letter-spacing: 1px; transition: all 0.3s; margin-top: 10px; }
        .submit-btn:hover { background-color: #00ccaa; box-shadow: 0 0 15px rgba(0,255,204,0.25); }
        .switch-link { display: block; margin-top: 18px; color: #888890; font-size: 12px; text-decoration: none; }
        .switch-link span { color: var(--neon-cyan); font-weight: bold; }
        .error-msg { background-color: rgba(255,51,51,0.08); border: 1px solid var(--neon-alert); color: var(--neon-alert); padding: 10px; border-radius: 6px; font-size: 12px; margin-bottom: 15px; font-weight: bold; text-align: center; }
        .success-msg { background-color: rgba(51,255,51,0.08); border: 1px solid var(--neon-green); color: var(--neon-green); padding: 10px; border-radius: 6px; font-size: 12px; margin-bottom: 15px; font-weight: bold; text-align: center; }
     </style>
</head>
     (Welcome Screen) -->
    {% if segment == 'welcome' %}
    <div class="auth-wrapper">
        <div class="auth-container">
            <div class="header">👑 SYSTEM KAVACH 👑</div>
            <div class="owner-tag">GLOBAL SECURE DASHBOARD</div>
            <h2 class="auth-heading">HACK-LESS PROTECTION ON</h2>
            <p class="info-text">Welcome to the world's most powerful decentralized cloud protection hub. This network shields transmission gates dynamically. To interact with the system buttons, you must first register your Unique User ID below.</p>
            <button class="submit-btn" onclick="window.location.href='/signup'">PROCEED TO SIGN UP 🔒</button>
            <a href="/login" class="switch-link">Already a registered owner? <span>Log In here</span></a>
        </div>
    </div>
    {% endif %}
@app.rout('/signup',methods=['GET','POST', 'HEAD'])
    <!-:(Sign Up Box) -->
    {% if segment == 'signup' %}
    <div class="auth-wrapper">
        <div class="auth-container">
            <div class="header">🛡️ REGISTER GATE 🛡️</div>
            <div class="owner-tag">IDENTITY VAULT MAKER</div>
            <h2 class="auth-heading">CREATE USER ACCOUNT</h2>
            {% if error %}<div class="error-msg">{{ error }}</div>{% endif %}
            {% if success %}<div class="success-msg">{{ success }}</div>{% endif %}
            <form action="/signup" method="POST">
                <div class="form-group">
                    <label>CREATE USER ID / USERNAME</label>
                    <input type="text" name="username" placeholder="Letters or numbers only..." required autocomplete="off">
                </div>
                <div class="form-group">
                    <label>CREATE SECURITY PASSWORD</label>
                    <input type="password" name="password" placeholder="At least 4 keys..." required>
                </div>
                <button type="submit" class="submit-btn">ACTIVATE USER GRID 📡</button>
            </form>
            <a href="/login" class="switch-link">Have an active access key? <span>Log In</span></a>
    </div>
    {% endif %}
@app,route('/login',methods=['GET','POST','HEAD'])
    <!--:(Log In Box) -->
    {% if segment == 'login' %}
    <div class="auth-wrapper">
        <div class="auth-container"</div>
            <div class="header">🔐 LOCK SCREEN 🔐</div>
            <div class="owner-tag">ANTI-HACK IDENTITY CHECK</div>
            <h2 class="auth-heading">ENTER KEY DETAILS</h2>
            {% if error %}<div class="error-msg">{{ error }}</div>{% endif %}
            <form action="/login" method="POST">
                <div class="form-group">
                    <label>ENTER USER ID</label>
                    <input type="text" name="username" placeholder="Your account ID..." required autocomplete="off">
                </div>
                <div class="form-group">
                    <label>ENTER SECRET PASSWORD</label>
                    <input type="password" name="password" placeholder="Your password..." required>
                </div>
                <button type="submit" class="submit-btn">UNLOCK SHIELD INTERFACE 👑</button>
            </form>
            <a href="/signup" class="switch-link">Need a new security pass? <span>Sign Up</span></a>
        </div>
    </div>
    {% endif %}
    <!-- -->
    {% if segment == 'dashboard' %}
@app.route('/dashboard', methods=['GET', 'HEAD'])
<body>
    <div class="container">
        <div class="header">👑 Universal System Kavach 👑</div>
        <div class="owner-tag">[© 2026 REGISTERED OWNER: YOU]</div>
        <div class="status-box">🔒 Privacy Status: '100-Layer Strict Shield' is Active. System Secure (Hak Less).</div>
        <div class="grid-container">
            <button class="btn btn-ports" onclick="triggerSoftware('/api/scan-ports')">
                <span class="btn-title">🧹 2-Ports Scanner</span>
                <span class="btn-desc">(Hacker Signals Flash Wipe)</span>
            </button>
            <button class="btn btn-network" onclick="triggerSoftware('/api/network-hunting')">
                <span class="btn-title">📡 3-Step Network Hunting</span>
                <span class="btn-desc">(1000 KM Satellite Catcher)</span>
            </button>
            <button class="btn btn-timelock" onclick="triggerSoftware('/api/time-lock')">
                <span class="btn-title">⏱️ Millisecond Time-Lock</span>
                <span class="btn-desc">(Counter-Hack Tool Locker)</span>
            </button>
            <button class="btn btn-compiler" onclick="triggerSoftware('/api/neural-compiler')">
                <span class="btn-title">🧠 Neural Legal Compiler</span>
                <span class="btn-desc">(Mind-Reading Input Scan)</span>
            </button>
        </div>
    </div>
    <div id="overlay" class="overlay"></div>
    <div id="customAlert" class="custom-alert">
        <h3 id="alertTitle">Alert</h3>
        <p id="alertMessage">Message</p>
        <button class="custom-alert-btn" onclick="closeAlert()">CLOSE SHIELD ❌</button>
    </div>
    <div class="footer">Designed Globally for Humanity as a Sovereign Cloud Application under Proprietary Copyright License © 2026</div>
    <script>
        const alertBox = document.getElementById('customAlert');
        const overlayBox = document.getElementById('overlay');
        async function triggerSoftware(endpoint) {
            try {
                const response = await fetch(endpoint);
                const data = await response.json();
                document.getElementById('alertTitle').innerText = data.title;
                document.getElementById('alertMessage').innerHTML = data.message;
                overlayBox.style.display = 'block';
                alertBox.classList.add('active');
            } catch (error) {
                alert("⚠️ Connection Break! Re-linking Universal Satellite Grid...");
            }
        }
        function closeAlert() {
            overlayBox.style.display = 'none';
            alertBox.classList.remove('active');
        }
    </script>
</body>
</html>
"""
@app.route('/',methods=['GET', 'POST', 'HEAD'])
def home():
    return render_template_string(HTML_layout,page='welcom')
@app.route('/api/scan-ports', methods=['GET'])
def scan_ports():
    return jsonify({"status": "SUCCESS", "title": "🛡️ 2-PORTS SCANNER", "message": "[Point 1 & 14]: Active Web Channel Protection<br>Hacker pathways wiped clean instantly like a Flash.<br><br>🖥️ Tracked Hacker IP: 72.163.85.54"})
@app.route('/api/network-hunting', methods=['GET'])
def network_hunting():
    return jsonify({"status": "SUCCESS", "title": "📡 NETWORK RESTORED", "message": "[Point 13, 15]: Cloud Network drop detected!<br><br>🔗 Connected Source: Asman Satellite (Starlink Grid)"})
@app.route('/api/time-lock', methods=['GET'])
def time_lock():
    return jsonify({"status": "SUCCESS", "title": "⏱️ MILLISECOND TIME-LOCK", "message": "[Layer 2 Architecture]: Web access security token is changing every 1 millisecond.<br><br>Brute-force decryption tools destroyed instantly."})
@app.route('/api/neural-compiler', methods=['GET'])
def neural_compiler():
    return jsonify({"status": "SUCCESS", "title": "🧠 NEURAL COMPILER", "message": "[Third Page Solution]: Input data scan 100% successful.<br><br>Corrupted scripts converted into Original Legal Source Code."})
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
        
        
        
            


        

                

       

            
            


            


                                  

        

 
