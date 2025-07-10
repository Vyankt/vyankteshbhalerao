# CI/CD Pipeline for Microservices on AWS ECS

This project demonstrates a complete CI/CD pipeline for a microservices-based application using AWS services and GitHub. The pipeline automatically builds, tests, and deploys containerized microservices to Amazon ECS with Fargate upon every push to the `main` branch.

## Architecture

The CI/CD pipeline follows this automated workflow:

1.  **Source:** A developer pushes code to a GitHub repository.
2.  **Trigger:** A GitHub webhook triggers the AWS CodePipeline.
3.  **Build:** AWS CodeBuild checks out the code, dynamically finds which microservice was changed (or builds all), runs tests (optional), builds a Docker image for each service, and pushes the image to Amazon ECR (Elastic Container Registry).
4.  **Deploy:** CodePipeline triggers an ECS deployment action, which updates the corresponding ECS service with the new Docker image, causing ECS to gracefully deploy the new version of the container in a rolling update.



## Project Structure

This repository is a monorepo containing multiple services and the CI/CD configuration.
