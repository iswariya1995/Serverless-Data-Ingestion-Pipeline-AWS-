import boto3

s3 = boto3.client('s3')

bucket_name = "your-bucket-name"
file_path = "customers.csv"

s3.upload_file(file_path, bucket_name, "uploads/customers.csv")

print("Upload successful")
