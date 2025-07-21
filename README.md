# Real‑Time Clickstream Analytics Pipeline

**Overview:**  
Simulate clickstream → Zookeeper & Kafka → Spark Structured Streaming → PostgreSQL → Grafana.

---

## Phases

### 1. Kafka, Zookeeper & Event Producer
- Deploy Zookeeper and Kafka (or Redpanda) to coordinate and broker click events.  
- Run a Python producer script to simulate user clickstream events and publish them to Kafka.

### 2. Spark Streaming Prototype
- Use Apache Spark Structured Streaming to consume click events from Kafka.  
- Prototype windowed aggregations and enrichments in micro‑batches.

### 3. Persist to PostgreSQL
- Write the aggregated metrics from Spark into a PostgreSQL table, optimized for time‑windowed queries.

### 4. Grafana Dashboard
- Import the exported JSON dashboard into Grafana.  
- Configure three panels:  
  1. Time‑series of click volume  
  2. Top 5 pages by clicks  
  3. Gauge of the latest window

### 5. Best Practices & Scaling
- Containerize components with Docker Compose and enable auto‑restart.  
- Tune Spark parallelism and Kafka partitioning.  
- Secure connections and credentials via environment variables or secrets management.

### 6. Publishing & Demo
- Commit all code, configurations, and dashboard JSON to GitHub.  
- Tag a release and share a screenshot.  
- Post a demo write‑up on LinkedIn for visibility.

---

## Prerequisites

- Docker & Docker Compose (for Zookeeper, Kafka, PostgreSQL)  
- Python 3.8+  
- Apache Spark 3.x (or 4.x with compatible Kafka package)  
- Java 17+  
- PostgreSQL 14+  
- Grafana 9+  
- Git & GitHub account

---

## Grafana Dashboard

The live dashboard JSON is in `dashboards/clickstream_dashboard.json`.

To import:  
1. In Grafana → **Dashboards** → **Import**  
2. Upload `dashboards/clickstream_dashboard.json`  
3. Select your PostgreSQL data source

---

## Live Dashboard Preview

![Real‑time clickstream analytics dashboard](docs/img/dashboard.png)  
*Figure: Real‑time clickstream analytics dashboard*  
