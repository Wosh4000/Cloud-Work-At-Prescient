import json

def lambda_handler(event, context):

    print(f"Received event: {event}")
        
    message = event.get('message', 'Hello from Lambda!')
        
    response = {
        "statusCode": 200,
        "body": json.dumps(f"Processed: {message}")
    }
    return response