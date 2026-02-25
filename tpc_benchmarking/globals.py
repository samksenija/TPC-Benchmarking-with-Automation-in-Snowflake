import snowflake.connector
import os

from dotenv import load_dotenv

load_dotenv() 

conn = snowflake.connector.connect(
    user=os.getenv("user"),
    password=os.getenv("password"),
    account=os.getenv("account"),
    warehouse=os.getenv("warehouse"),
    database=os.getenv("database"),
    schema=os.getenv("schema")
)

#this is global configuration of database & schema
database = f"""
        USE DATABASE SNOWFLAKE_SAMPLE_DATA;
    """

schema = f"""
        USE SCHEMA TPCH_SF100;
    """
cursor = conn.cursor()

database_definition = cursor.execute(database)
schema_definition = cursor.execute(schema)

#1.py
d = 1
upper_limit = 31

    
