from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col, window
from pyspark.sql.types import StructType, IntegerType, StringType, LongType

# 1) Define the click event schema
schema = StructType() \
    .add("user_id", IntegerType()) \
    .add("page", StringType()) \
    .add("timestamp", LongType())

# 2) Build SparkSession
spark = SparkSession.builder \
    .appName("ClickStreamAnalytics") \
    .getOrCreate()

# 3) Read from Kafka
raw_df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "clicks") \
    .option("startingOffsets", "latest") \
    .load()

# 4) Parse JSON payload and add a timestamp column
events = raw_df.select(
    from_json(col("value").cast("string"), schema).alias("data")
).select("data.*") \
  .withColumn("event_time", (col("timestamp")/1000).cast("timestamp"))

# 5) Windowed count per page (1‑minute tumbling window)
counts = events.groupBy(
    window(col("event_time"), "1 minute"),
    col("page")
).count().orderBy("window")

# 6) Write results to console
query = counts.writeStream \
    .outputMode("complete") \
    .format("console") \
    .option("truncate", False) \
    .start()

query.awaitTermination()
