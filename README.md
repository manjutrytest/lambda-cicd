# lambda-cicd
When you push code to GitHub, CodePipeline triggers CodeBuild to create a deployment ZIP, then CodePipeline deploys the ZIP to an existing AWS Lambda function automatically.

# Lambda CI/CD Example

This repository contains:
- `lambda_function.py` – Python Lambda function handler  
- `buildspec.yml` – CodeBuild configuration to create `deployment-package.zip`

## Lambda Settings

Set the following in AWS Lambda:

- **Runtime:** Python 3.9  
- **Handler:** `lambda_function.lambda_handler`

## Local Packaging


