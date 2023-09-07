import boto3
import os

def buckets():
    """
    S3 buckets
    """
    pass

@buckets.command()
def create():
    s3 = boto3.client(
        "s3",
        config=boto3.session.Config(signature_version="s3v4"),
        region_name="eu-central-1",
        endpoint_url=os.getenv("S3_ENDPOINT_URL", "http://localhost:9000"),
        aws_access_key_id=os.getenv(
            "S3_DATA_ACCESS_KEY", "ACS"
        ),
        aws_secret_access_key=os.getenv(
            "S3_DATA_SECRET_KEY", "SCRTSCRT"
        ),
    )
