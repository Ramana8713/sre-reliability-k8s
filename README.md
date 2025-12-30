# sre-reliability-k8s

## Overview
Reliability-driven Kubernetes service demonstrating SLIs, SLOs, error budgets, and auto-remediation.

## Architecture
- Flask Python service with 10% failure rate
- Kubernetes deployment with liveness/readiness probes
- Horizontal Pod Autoscaler for CPU-based scaling
- Prometheus metrics + Alertmanager for SLO-based alerting
- Grafana dashboards to visualize SLIs and error budgets

## SLIs & SLOs
- Availability ≥ 99.5%
- Latency p95 ≤ 1.5s
- Error budget = 0.5%

## Monitoring & Alerts
- Prometheus scrapes metrics on `/metrics` (port 8000)
- Alert fires when error rate > 2% for 2 min

## Failure Scenarios Tested
- Random application errors
- Pod crashes
- Latency spikes
