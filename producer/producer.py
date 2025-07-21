from confluent_kafka import Producer
import json, random, time, socket

# ——— Configure the Kafka client ———
conf = {
    'bootstrap.servers': 'localhost:9092',
    'client.id': socket.gethostname()
}
producer = Producer(conf)

# ——— Event generator ———
def generate_event():
    ev = {
        'user_id': random.randint(1, 1000),
        'page': random.choice(['home', 'search', 'product', 'cart', 'checkout']),
        'timestamp': int(time.time() * 1000)
    }
    print("👉 Generated event:", ev)
    return ev

# ——— Delivery callback ———
def delivery_callback(err, msg):
    if err:
        print("❌ Delivery failed:", err)
    else:
        print(f"✅ Delivered to {msg.topic()} [{msg.partition()}] @ offset {msg.offset()}")

# ——— Main loop ———
if __name__ == "__main__":
    topic = 'clicks'
    print(f"🚀 Starting producer for topic '{topic}' (Ctrl+C to stop)…")
    try:
        while True:
            event = generate_event()
            # Send to Kafka
            producer.produce(topic, json.dumps(event), callback=delivery_callback)
            # Serve delivery reports (blocking up to 1s)
            producer.poll(1.0)
            # Throttle event rate
            time.sleep(0.5)  # ~2 events/sec
    except KeyboardInterrupt:
        print("\n⏹️  Interrupted—flushing pending messages…")
        producer.flush(10)
        print("✅ Shutdown complete")
