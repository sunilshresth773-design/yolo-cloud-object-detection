import json
import boto3

# Replace with your actual EC2 Instance ID
ec2_instance_id = "i-0cefa3ba4f0a6f8fe"

ssm = boto3.client("ssm")

def lambda_handler(event, context):
    try:
        body = json.loads(event.get("body", "{}"))
        image_name = body.get("image_name")

        if not image_name:
            return {
                "statusCode": 400,
                "body": json.dumps({"error": "image_name is required"})
            }

        command = f"python3 /home/ec2-user/yolov5/s3_yolo.py {image_name}"

        response = ssm.send_command(
            InstanceIds=[ec2_instance_id],
            DocumentName="AWS-RunShellScript",
            Parameters={
                "commands": [command]
            },
        )

        return {
            "statusCode": 200,
            "body": json.dumps({
                "message": "YOLO detection started",
                "command_id": response["Command"]["CommandId"]
            })
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }