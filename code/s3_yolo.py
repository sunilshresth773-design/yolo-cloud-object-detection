import boto3
import subprocess
import sys
import os

# AWS S3 bucket details
BUCKET_NAME = "object-detection-sunil-2026"
INPUT_FOLDER = "input/"
OUTPUT_FOLDER = "output/"

s3 = boto3.client("s3")

def download_image(image_name):
    local_path = f"/home/ec2-user/yolov5/{image_name}"
    s3.download_file(BUCKET_NAME, INPUT_FOLDER + image_name, local_path)
    return local_path

def upload_result(image_name):
    result_path = f"/home/ec2-user/yolov5/runs/detect/exp/{image_name}"
    if os.path.exists(result_path):
        s3.upload_file(result_path, BUCKET_NAME, OUTPUT_FOLDER + image_name)

def run_yolo(image_path):
    command = [
        "python3",
        "detect.py",
        "--weights", "yolov5s.pt",
        "--source", image_path,
        "--project", "runs/detect",
        "--name", "exp",
        "--exist-ok"
    ]
    subprocess.run(command)

if __name__ == "__main__":
    image_name = sys.argv[1]
    image_path = download_image(image_name)
    run_yolo(image_path)
    upload_result(image_name)