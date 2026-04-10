import psutil
import time
from datetime import datetime

def get_stats():
    cpu = psutil.cpu_percent(interval=1)
    mem = psutil.virtual_memory()
    disk = psutil.disk_usage('/')
    timestamp = datetime.now().strftime("%H:%M:%S")
    
    return {
        "cpu": cpu,
        "mem": mem.percent,
        "disk": disk.percent,
        "time": timestamp
    }

def update_html(data):
    html = f'''
    <html>
    <head>
    <meta http-equiv="refresh" content="2">
    <style>
    body {{ background:#0d1117; color:#58a6ff; font-family:Arial; text-align:center; }}
    .box {{ background:#161b22; padding:20px; margin:50px auto; width:300px; border-radius:10px; }}
    </style>
    </head>
    <body>
        <div class="box">
            <h2>InfraWatch Lite</h2>
            <p>CPU: {data['cpu']}%</p>
            <p>RAM: {data['mem']}%</p>
            <p>DISK: {data['disk']}%</p>
            <p>Atualizado: {data['time']}</p>
        </div>
    </body>
    </html>
    '''
    with open("index.html", "w") as f:
        f.write(html)

while True:
    stats = get_stats()

    print(f"CPU: {stats['cpu']}% | RAM: {stats['mem']}% | DISK: {stats['disk']}%")

    with open("log.txt", "a") as f:
        f.write(str(stats) + "\n")

    update_html(stats)

    time.sleep(2)
