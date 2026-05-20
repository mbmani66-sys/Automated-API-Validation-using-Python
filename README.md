Automated API Validation using Python (DevOps CI/CD
 Project)

Project Overview

This project is a DevOps-based automation system that
validates APIs using Python, containerizes the
application using Docker, and deploys it using a 
CI/CD pipeline via GitHub Actions and AWS services.

It eliminates manual API testing and ensures
 consistent validation across environments.

- API testing is done manually using tools like Postman
- QA teams miss test cases if done manually
- Inconsistent API behavior across environments
 (dev/stage/prod)
- Deployment happens without proper validation

 This leads to production bugs and delays.


This projec provides solution to automates the entire
API validation and deployment process:

- Python script validates APIs automatically
- Docker container ensures environment consistency
- GitHub Actions runs CI/CD pipeline
- AWS hosts and stores containerized application

Create a file named
->nano app.py
->nano tests.json

To test run
python3 app.py

Initialize Git repository
->git init
->git remote add origin <your-github-repo-url>

Push code to
-> git add .
-> git commit -m "Initi... "
-> git push -u origin main

Python Module

- API request validation
- Status code verification
- Response key validation
- Error handling for failed APIs

AWS Services Used

Launch Amazon EC2
- Used as deployment server
- Runs Docker container

Create Amazon ECR in AWS
- Stores Docker images securely
- Used by CI/CD pipeline for image push/pull

IAM (Identity & Access Management)
- Provides secure access to AWS resources
- Used for GitHub Actions authentication

Docker setup 
-> docker build -t api-validator .
-> docker run api-validator

Setup GitHub actions CI/CD
Create a file -> .github/workflows/ci-cd.yml

This above pipeline with run python tests like build 
the docker image push it to AWS ECR and deploy it to 
EC2.


