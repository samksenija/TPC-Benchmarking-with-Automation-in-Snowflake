import snowflake.connector

conn = snowflake.connector.connect(
    user='user',
    password='password',
    account='your_account',
    warehouse='your_warehouse',
    database='your_database',
    schema='your_schema'
)

#this is global configuration of database & schema
database_schema = f"""
        USE DATABASE SNOWFLAKE_SAMPLE_DATA;
        USE SCHEMA TPCH_SF100;
    """
