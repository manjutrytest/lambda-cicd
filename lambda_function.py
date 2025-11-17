import json
import datetime

def lambda_handler(event, context):
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Hello from Lambda deployed via CodePipeline by manju!",
            "deployed_at": datetime.datetime.utcnow().isoformat() + "Z",
            "event": event
        })
    }
