import boto3
import json
import os

sns_client = boto3.client('sns')
topic_arn = os.environ['arn:aws:sns:us-east-1:533629863969:S3BucketChangeNotifications']

def lambda_handler(event, context):
    print("Received event:", json.dumps(event, indent=2))
    
    for record in event['Records']:
        bucket = record['s3']['bucket']['name']
        key = record['s3']['object']['key']
        event_name = record['eventName']
        event_time = record['eventTime']

        message = (
            f"S3 Bucket Change Detected:\n"
            f"- Event: {event_name}\n"
            f"- Bucket: {bucket}\n"
            f"- Key: {key}\n"
            f"- Time: {event_time}"
        )
        
        sns_client.publish(
            TopicArn=topic_arn,
            Subject="S3 Bucket Change Notification",
            Message=message
        )
