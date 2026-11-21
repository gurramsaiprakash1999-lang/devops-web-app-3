from flask import Flask, render_template_string
import platform
import socket
import datetime

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CyberSecurity Operations Hub</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
    <style>
        body {
            background-color: #050811;
            color: #e2e8f0;
            font-family: 'Segoe UI', Consolas, monospace;
            min-height: 100vh;
        }
        .navbar-brand {
            font-weight: 800;
            font-size: 1.6rem;
            background: linear-gradient(135deg, #00f2fe, #4facfe);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        .card-custom {
            background: #0d1527;
            border: 1px solid #1e293b;
            border-radius: 12px;
            box-shadow: 0 8px 24px rgba(0, 242, 254, 0.08);
            transition: all 0.25s ease-in-out;
        }
        .card-custom:hover {
            transform: translateY(-5px);
            border-color: #00f2fe;
            box-shadow: 0 12px 30px rgba(0, 242, 254, 0.2);
        }
        .status-badge {
            padding: 6px 16px;
            border-radius: 20px;
            font-size: 0.85rem;
            font-weight: 600;
            background: rgba(16, 185, 129, 0.15);
            color: #10b981;
            border: 1px solid #10b981;
        }
        .hero-title {
            font-size: 2.8rem;
            font-weight: 800;
            background: linear-gradient(135deg, #00f2fe, #38ef7d, #00c6ff);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        .cyber-icon {
            font-size: 2.2rem;
            color: #00f2fe;
        }
    </style>
</head>
<body>
    <nav class="navbar navbar-expand-lg border-bottom border-secondary mb-4 py-3">
        <div class="container">
            <a class="navbar-brand" href="#"><i class="fa-solid fa-shield-halved text-info"></i> CYBERSECURITY OPERATIONS CENTER</a>
            <span class="status-badge"><i class="fa-solid fa-lock"></i> SYSTEM SECURE</span>
        </div>
    </nav>

    <div class="container pb-5">
        <div class="text-center mb-5">
            <h1 class="hero-title">CyberSecurity Command Portal</h1>
            <p class="text-secondary fs-5">Real-Time Threat Monitoring & DevSecOps Infrastructure Protection</p>
        </div>

        <!-- Live Security Diagnostics -->
        <div class="row g-4 mb-5">
            <div class="col-md-4">
                <div class="card-custom p-4">
                    <div class="cyber-icon mb-2"><i class="fa-solid fa-user-shield"></i></div>
                    <h5 class="text-secondary fs-6 text-uppercase">Environment Status</h5>
                    <h4 class="fw-bold text-light">{{ info.os }}</h4>
                    <p class="mb-0 text-muted fs-7">Secure Node: {{ info.hostname }}</p>
                </div>
            </div>
            <div class="col-md-4">
                <div class="card-custom p-4">
                    <div class="cyber-icon mb-2 text-success"><i class="fa-solid fa-network-wired"></i></div>
                    <h5 class="text-secondary fs-6 text-uppercase">Protected Pod IP</h5>
                    <h4 class="fw-bold text-light">{{ info.ip }}</h4>
                    <p class="mb-0 text-muted fs-7">Kubernetes Isolated Network</p>
                </div>
            </div>
            <div class="col-md-4">
                <div class="card-custom p-4">
                    <div class="cyber-icon mb-2 text-warning"><i class="fa-solid fa-stopwatch"></i></div>
                    <h5 class="text-secondary fs-6 text-uppercase">Security Engine Time</h5>
                    <h4 class="fw-bold text-light">{{ info.time }} UTC</h4>
                    <p class="mb-0 text-muted fs-7">Real-Time Scan Active</p>
                </div>
            </div>
        </div>

        <!-- Core Security Modules -->
        <h4 class="fw-bold mb-3 text-light"><i class="fa-solid fa-cubes-stacked text-info"></i> Active DevSecOps Protection Modules</h4>
        <div class="row g-3">
            <div class="col-6 col-md-2">
                <div class="card-custom p-3 text-center">
                    <i class="fa-solid fa-eye fa-2x text-info mb-2"></i>
                    <h6 class="mb-0">SIEM Monitor</h6>
                </div>
            </div>
            <div class="col-6 col-md-2">
                <div class="card-custom p-3 text-center">
                    <i class="fa-solid fa-bug-slash fa-2x text-danger mb-2"></i>
                    <h6 class="mb-0">Vulnerability Scan</h6>
                </div>
            </div>
            <div class="col-6 col-md-2">
                <div class="card-custom p-3 text-center">
                    <i class="fa-brands fa-docker fa-2x text-info mb-2"></i>
                    <h6 class="mb-0">Docker Hardened</h6>
                </div>
            </div>
            <div class="col-6 col-md-2">
                <div class="card-custom p-3 text-center">
                    <i class="fa-solid fa-dharmachakra fa-2x text-primary mb-2"></i>
                    <h6 class="mb-0">K8s Network Rules</h6>
                </div>
            </div>
            <div class="col-6 col-md-2">
                <div class="card-custom p-3 text-center">
                    <i class="fa-solid fa-key fa-2x text-warning mb-2"></i>
                    <h6 class="mb-0">IAM Policy</h6>
                </div>
            </div>
            <div class="col-6 col-md-2">
                <div class="card-custom p-3 text-center">
                    <i class="fa-brands fa-jenkins fa-2x text-danger mb-2"></i>
                    <h6 class="mb-0">Jenkins (Java 21)</h6>
                </div>
            </div>
        </div>
    </div>
</body>
</html>
"""

@app.route('/')
def cyber_sec():
    sys_info = {
        'os': f"{platform.system()} {platform.release()}",
        'hostname': socket.gethostname(),
        'ip': socket.gethostbyname(socket.gethostname()),
        'time': datetime.datetime.now().strftime("%H:%M:%S")
    }
    return render_template_string(HTML_TEMPLATE, info=sys_info)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
