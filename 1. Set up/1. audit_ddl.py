# Databricks notebook source
# MAGIC %sql
# MAGIC CREATE CATALOG IF NOT EXISTS tt_hc_adb_ws;

# COMMAND ----------

# DBTITLE 1,Untitled
# MAGIC %sql
# MAGIC CREATE DATABASE IF NOT EXISTS tt_hc_adb_ws.audit;

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE TABLE IF NOT EXISTS tt_hc_adb_ws.audit.load_logs (
# MAGIC     data_source STRING,
# MAGIC     tablename STRING,
# MAGIC     numberofrowscopied INT,
# MAGIC     watermarkcolumnname STRING,
# MAGIC     loaddate TIMESTAMP
# MAGIC );

# COMMAND ----------

# MAGIC %sql
# MAGIC truncate table  tt_hc_adb_ws.audit.load_logs;

# COMMAND ----------

# MAGIC %sql 
# MAGIC select * from tt_hc_adb_ws.audit.load_logs;
