from flask import Flask
import random, time
from prometheus_client import Counter, Histogram, start_http_server

app = Flask(__name__)

# Metrics
REQUESTS = Counter('http_requests_total', 'Total HTTP requests', ['status'])
LATENCY = Histogram('http_request_latency_seconds', 'Request latency')

@app.route("/")
def home():
    # Inject 10% failure rate
    if random.random() < 0.1:
        REQUESTS.labels(status="500").inc()
        return "Internal Error", 500

    with LATENCY.time():
        time.sleep(random.uniform(0.1, 1.5))

    REQUESTS.labels(status="200").inc()
    return "OK"

if __name__ == "__main__":
    # Expose metrics on port 8000
    start_http_server(8000)
    app.run(host="0.0.0.0", port=5000)
