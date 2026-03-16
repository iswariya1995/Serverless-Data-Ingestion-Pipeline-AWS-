# Serverless Data Ingestion Pipeline (AWS)

An event-driven **serverless data ingestion pipeline** built on AWS.  
Automatically processes CSV files uploaded to Amazon S3, inserts the data into Amazon RDS, sends notifications via Amazon SNS, and logs execution using CloudWatch.

---

## Architecture

![AWS Serverless Pipeline](images/architecture.png)


---

## AWS Services Used

| Service | Purpose |
|--------|---------|
| Amazon S3 | File storage for uploaded CSV files |
| AWS Lambda | Serverless compute for processing CSV files |
| Amazon RDS | Relational database storage |
| Amazon SNS | Email notifications for success/failure |
| Amazon CloudWatch | Logging and monitoring Lambda executions |
| IAM | Secure access control |

---

## Project Structure

```text
aws-serverless-data-pipeline/
│
├── lambda/
│   └── lambda_function.py
├── scripts/
│   └── upload_to_s3.py
├── sql/
│   └── schema.sql
├── sample-data/
│   └── customers.csv
└── README.md
---
## Workflow

1. Upload CSV file to an **S3 bucket**.
2. **S3 event notification** triggers Lambda.
3. Lambda downloads and parses the CSV.
4. Lambda inserts records into the **RDS database**.
5. Lambda triggers **SNS notification** (success/failure).
6. Execution logs stored in **CloudWatch**.

---

## Sample CSV

id,first_name,last_name,email
1,John,Doe,john.doe@example.com
2,Jane,Smith,jane.smith@example.com
3,Ahmed,Khan,ahmed.khan@example.com

---

### Required Policies

- `AmazonS3ReadOnlyAccess`
- `AmazonRDSFullAccess`
- `AmazonSNSFullAccess`
- `AWSLambdaBasicExecutionRole`

---

## Networking

Lambda must run inside a **VPC** to connect to the RDS database.

### Required Configuration

- VPC
- Private subnets
- Security group allowing Lambda access to RDS

---

## Monitoring

Monitoring is configured using **CloudWatch**.

### Features

- Lambda execution logs
- Error tracking
- Metric filters
- Alarms for failed executions

---

## Optional Enhancements

Potential improvements for production environments:

- File validation before database insertion
- Support for JSON or XML data formats
- Use AWS Secrets Manager for database credentials
- Use AWS Step Functions for workflow orchestration
- Implement CI/CD deployment pipelines
- Infrastructure as Code using Terraform or CloudFormation

---

## Learning Outcomes

This project demonstrates:

- Event-driven architecture
- Serverless backend processing
- AWS service integration
- Automated notification systems
- Monitoring and logging of serverless applications

---

## Summary

This project implements an automated **serverless data ingestion pipeline** that integrates multiple AWS services to process files and store structured data in a relational database.

It simulates real-world enterprise workflows such as:

- Automated reporting
- E-commerce data ingestion
- CRM data synchronization
