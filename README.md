# Cloud-Based Image Object Detection System

## Project Overview

This project implements a cloud-based image object detection system using YOLOv5 and AWS cloud services. The system detects objects in images uploaded to Amazon S3 and processes them using a YOLOv5 model hosted on an EC2 instance.

The detection workflow is orchestrated using AWS Lambda and exposed through API Gateway.

---

## Technologies Used

- YOLOv5 (Pre-trained on COCO dataset)
- AWS EC2 (Model Hosting)
- AWS Lambda (Serverless Controller)
- API Gateway (Public API Endpoint)
- Amazon S3 (Input & Output Storage)
- AWS Systems Manager (SSM)

---

## Architecture

User → API Gateway → Lambda → SSM → EC2 (YOLOv5) → S3 (Output)

---

## How It Works

1. The user uploads an image to the S3 `input/` folder.
2. A POST request is sent to the API endpoint.
3. API Gateway triggers the Lambda function.
4. Lambda sends a secure command to EC2 via AWS SSM.
5. EC2 runs YOLOv5 detection on the image.
6. The processed image is saved in the S3 `output/` folder.

---

## Live API Endpoint

POST Request:
https://ubc567q60a.execute-api.us-east-1.amazonaws.com/detect

Example JSON Body:

{
  "image_name": "car.jpg"
}

---

## Dataset

The YOLOv5 model used in this project is pre-trained on the COCO (Common Objects in Context) dataset:

https://cocodataset.org/

---

## Repository Structure
