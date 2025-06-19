import pymysql
import boto3
import csv
import os
from io import StringIO

# RDS Configuration
rds_host = "database-2.cpu8cy2ykgg9.eu-north-1.rds.amazonaws.com"
db_user = "admin"
db_password = "dilli987"
db_name = "hello"

# S3 Configuration
s3_bucket = "sql-lambda-bucket"
s3_key = "output/students.csv"

def lambda_handler(event, context):
    try:
        # Connect to RDS
        conn = pymysql.connect(
            host=rds_host,
            user=db_user,
            password=db_password,
            db=db_name,
            connect_timeout=10
        )
        
        cursor = conn.cursor()
        cursor.execute("SELECT *  FROM students")
        rows = cursor.fetchall()
        
        # Convert to CSV
        csv_buffer = StringIO()
        csv_writer = csv.writer(csv_buffer)
        csv_writer.writerow(["StudentId", "LirstName","LastName","JoiningDate","Department", "Gender"])
        csv_writer.writerows(rows)
        
        # Upload to S3
        s3 = boto3.client('s3')
        s3.put_object(Bucket=s3_bucket, Key=s3_key, Body=csv_buffer.getvalue())
        
        return {
            'statusCode': 200,
            'body': f"CSV file uploaded successfully to s3://{s3_bucket}/{s3_key}"
        }
    
    except Exception as e:
        return {
            'statusCode': 500,
            'body': f"Error: {str(e)}"
        }
