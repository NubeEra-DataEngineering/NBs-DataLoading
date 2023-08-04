# Databricks notebook source
dbutils.fs.help()

# COMMAND ----------

dbutils.fs.ls("/tmp/")

# COMMAND ----------

dbutils.fs.put("/tmp/abc.txt","Welcome to Databricks File System",True)

# COMMAND ----------

dbutils.fs.help("mkdirs")

# COMMAND ----------

dbutils.fs.ls("s3://bucketname/folder/file.ext")

spark.read.format("parquet").load("s3://bucketname/folder/parquet")

spark.sql("SELECT * FROM parquet.`s3://bucketname/folder/file.parquet`")

# COMMAND ----------

# MAGIC %sh
# MAGIC databricks secrets list-scopes
# MAGIC # databricks secrets create-scope --scope mydata

# COMMAND ----------

strS3ObjectPath="s3://bkt-04aug-mujahed/workstation_env.yml"
dbutils.fs.ls(strS3ObjectPath)

# COMMAND ----------

# MAGIC %fs ls /databricks-datasets/structured-streaming/events/

# COMMAND ----------

# MAGIC %sh
# MAGIC pwd

# COMMAND ----------

# MAGIC %sh
# MAGIC git status

# COMMAND ----------

dbutils.fs.ls("s3://dasfsdcf3dw3edw3dfds/workstation_env.yml")

# COMMAND ----------

spark.sql("SELECT * from parquet.`s3://bkt-04aug-mujahed/userdata1.parquet`")

# COMMAND ----------


