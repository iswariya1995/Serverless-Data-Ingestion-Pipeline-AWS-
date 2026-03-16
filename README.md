# # Serverless Data Ingestion Pipeline (AWS)

## 🌟 Objective
Implement an **event-driven data ingestion pipeline** on AWS that automatically processes files uploaded from a local machine:

1. Upload to an **S3 bucket**.  
2. Processed by an **AWS Lambda function**.  
3. Inserted into an **RDS database**.  
4. Triggers an **SNS notification** on success or failure.  

---

## 📂 Architecture Overview


### Services Used

- **Amazon S3** – Store uploaded files.  
- **AWS Lambda** – Serverless compute for processing files.  
- **Amazon RDS** – Relational database (PostgreSQL or MySQL).  
- **Amazon SNS** – Email notifications for success/failure.  
- **Amazon CloudWatch** – Logging and monitoring.  
- **IAM** – Role and policy management for secure access.  

---

## 🔄 Workflow

1. CSV file uploaded to an S3 bucket from a local machine.  
2. S3 event triggers the Lambda function.  
3. Lambda reads and parses the CSV, connecting to RDS.  
4. Data inserted into a **customers** table in RDS.  
5. SNS sends success or failure notification.  
6. CloudWatch logs Lambda activity for auditing and debugging.  

---

## 📅 Use Case

Ideal for organizations receiving remote data (e.g., customer orders, product listings) that must be automatically ingested into backend databases for:

- Analytics  
- Reporting  
- CRM synchronization  

---

## Required IAM Policies

- `AmazonS3ReadOnlyAccess`  
- `AmazonRDSFullAccess`  
- `AmazonSNSFullAccess`  
- `AWSLambdaBasicExecutionRole`  

---

## Networking

Lambda must run inside a **VPC** to access the RDS database.

### Required Configuration

- VPC with private subnets  
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

Potential improvements for production:

- Validate files before inserting into the database  
- Support for JSON or XML data formats  
- Use **AWS Secrets Manager** for database credentials  
- Orchestrate workflows using **AWS Step Functions**  
- Implement CI/CD pipelines  
- Infrastructure as Code using **Terraform** or **CloudFormation**  

---

## Learning Outcomes

This project demonstrates:

- Event-driven architecture design  
- Serverless backend processing  
- AWS service integration  
- Automated notifications  
- Monitoring and logging for serverless applications  

---

## Summary

This project implements an automated **serverless data ingestion pipeline** that integrates multiple AWS services to process files and store structured data in a relational database.  

It simulates real-world enterprise workflows such as:

- Automated reporting  
- E-commerce data ingestion  
- CRM data synchronization 
