# main.py
import time
import boto3
import datetime
import json
import daemon

# AWS credentials (Add your IAM user credentials here)
AWS_ACCESS_KEY_ID = "YOUR_ACCESS_KEY_ID"
AWS_SECRET_ACCESS_KEY = "YOUR_SECRET_ACCESS_KEY"
AWS_REGION = "us-east-1"

# Initialize AWS clients
ec2_client = boto3.client("ec2", aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_ACCESS_KEY, region_name=AWS_REGION)
s3_client = boto3.client("s3", aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_ACCESS_KEY, region_name=AWS_REGION)

# set config.json for it 
with open("config.json") as f:
    config = json.load(f)

ec2_instances = config["ec2_instances"]
s3_buckets = config["s3_buckets"]
inactivity_threshold_minutes = config["inactivity_threshold_minutes"]

# Function to stop an EC2 instance
def stop_ec2_instance(instance_id):
    ec2_client.stop_instances(InstanceIds=[instance_id])

# Function to disable public access for an S3 bucket
def disable_s3_bucket_public_access(bucket_name):
    s3_client.put_public_access_block(
        Bucket=bucket_name,
        PublicAccessBlockConfiguration={
            "BlockPublicAcls": True,
            "IgnorePublicAcls": True,
            "BlockPublicPolicy": True,
            "RestrictPublicBuckets": True,
        },
    )

def check_ec2_inactivity(threshold_minutes, exceptions=None):
    # Code to get a list of running EC2 instances and their last activity timestamps
    # For demonstration purposes, we'll use a dummy list of instances and activity timestamps
    instance_activity = {
        "i-1234567890abcdef0": datetime.datetime.now() - datetime.timedelta(minutes=5),
        "i-abcdef1234567890": datetime.datetime.now() - datetime.timedelta(minutes=15),
    }

    # Filter instances based on inactivity threshold and exceptions
    inactive_instances = []
    current_time = datetime.datetime.now()
    for instance_id, last_activity_time in instance_activity.items():
        time_since_last_activity = (current_time - last_activity_time).total_seconds() / 60
        if time_since_last_activity >= threshold_minutes and instance_id not in (exceptions or []):
            inactive_instances.append(instance_id)

    return inactive_instances

def check_s3_inactivity(threshold_minutes):
    # Code to get a list of S3 buckets and their last activity timestamps
    bucket_activity = {
        "example-bucket-1": datetime.datetime.now() - datetime.timedelta(minutes=8),
        "example-bucket-2": datetime.datetime.now() - datetime.timedelta(minutes=20),
    }

    # Filter buckets based on inactivity threshold
    inactive_buckets = []
    current_time = datetime.datetime.now()
    for bucket_name, last_activity_time in bucket_activity.items():
        time_since_last_activity = (current_time - last_activity_time).total_seconds() / 60
        if time_since_last_activity >= threshold_minutes:
            inactive_buckets.append(bucket_name)

    return inactive_buckets

def main():
    while True:
        # Check EC2 instances for inactivity and stop if inactive
        inactive_ec2_instances = check_ec2_inactivity(inactivity_threshold_minutes, exceptions=ec2_instances)
        for instance_id in inactive_ec2_instances:
            stop_ec2_instance(instance_id)
            print(f"Stopped EC2 instance: {instance_id}")

        # Check S3 buckets for inactivity and disable public access if inactive
        inactive_s3_buckets = check_s3_inactivity(inactivity_threshold_minutes)
        for bucket_name in inactive_s3_buckets:
            disable_s3_bucket_public_access(bucket_name)
            print(f"Disabled public access for S3 bucket: {bucket_name}")

        time.sleep(300)  # Repeat every 5 minutes

if __name__ == "__main__":
    main()
