# Databricks notebook source
access_key = "AKIAW5IZRWOY7KOP4D47"
secret_key = "OsnS/To2mqtWyX3U3y6SB0cVr14OIHFWh5jf95rF"

#Mount bucket on databricks
encoded_secret_key = secret_key.replace("/", "%2F")

aws_bucket_name = "bkt-nithin-04aug"

mount_name = "nithinawss3"

dbutils.fs.mount("s3a://%s:%s@%s" % (access_key, encoded_secret_key, aws_bucket_name), "/mnt/%s" % mount_name)

display(dbutils.fs.ls("/mnt/%s" % mount_name))

mount_name = "nithinawss3"

file_name="iris.csv"

df = spark.read.format("csv").load("/mnt/%s/%s" % (mount_name , file_name))

df.show()

# COMMAND ----------

strMountPoint="/mnt/%s/%s" % (mount_name , file_name)

dbutils.fs.put(strMountPoint+"/abc.txt","Welcome to Text File",True)

# COMMAND ----------

strMountPointParquetFile="/mnt/%s/abc.parquet" % (mount_name)
df.write.parquet(strMountPointParquetFile)

# COMMAND ----------


