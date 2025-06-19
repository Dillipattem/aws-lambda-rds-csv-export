📊 Daily Employee Report Automation using AWS Lambda, RDS & S3
This project automates the process of extracting employee data from an Amazon RDS (MySQL) database, converting it to CSV, and uploading it to Amazon S3 — completely serverless using AWS Lambda.


Workflow:

Lambda connects to Amazon RDS (MySQL)

Executes a SELECT query to fetch Student data  (amy table in Database)

Generates a .csv file

Uploads the file to Amazon S3 at /daily-reports/Student_YYYYMMDD.csv

📁 Project Structure
bash
Copy
Edit
.
├── Rds-lambda-S3.py   # Main Lambda function code
├── diagram.png          # Architecture diagram
└── README.md            # Project documentation


🚀 Technologies Used
AWS Lambda

Amazon RDS (MySQL)

Amazon S3

Python (Boto3, PyMySQL)

IAM Roles

🔧 Setup Instructions
Deploy RDS (MySQL) with your employee data.

Create an S3 Bucket for storing CSV files.

Configure IAM Role with access to RDS and S3.

Deploy Lambda with lambda_function.py.

📅 Example Output
/daily-reports/Student_20250619.csv

📜 SQL Sample
SELECT id, name, department, salary FROM employees;
