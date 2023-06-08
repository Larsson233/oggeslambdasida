import json                     # used for converting json strings to Python objects
import boto3                    # handles AWS
from datetime import datetime   # used for creating the timestamp

def lambda_handler(event, context):
    # Connect to the DynamoDB table
    db = boto3.resource('dynamodb')
    table = db.Table('oggeslambdatable')

    # Create the time stamp
    dateTime = (datetime.now()).strftime("%Y-%m-%d %H:%M:%S")
    
    try:
        # Get the contact info from the request
        payload = json.loads(event['body'])
    
        # Add a row with contact info to DynamoDB
        table.put_item(
          Item={
          'timestamp': dateTime,
          'name': payload['name'],
          'email': payload['email'],
          'message': payload['msg']
          }
        )
        
        # Return success
        return {
            'statusCode': 200,
            'body': json.dumps('Successfully saved contact info!'),
            'headers': {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Credentials": True,
            }
        }
        
    except:
        # Return error
        return {
                'statusCode': 400,
                'body': json.dumps('Error saving contact info'),
                'headers': {
                    "Access-Control-Allow-Origin": "*",
                    "Access-Control-Allow-Credentials": True,
                }
        }