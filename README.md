# Security Quiz Docker Demonstration

This repository contains a simple interactive Python application created for testing and demonstration purposes. It shows how to containerize a basic application using Docker and distribute it to team members with minimal installation requirements.

## Purpose

This is a **test repository** designed to demonstrate:
1. Docker containerization
2. GitHub collaboration workflows
3. Easy distribution of applications

## Project Structure
```
├── app.py              # Simple interactive Python security quiz
└── Dockerfile          # Docker configuration for containerization
```
## Running the Application

### Local Python (requires Python installation)

```bash
python app.py 
```

### Using Docker (recommended)
Option 1: Build from source
```bash
# Build the Docker image
docker build -t security-quiz .

# Run the container interactively
docker run -it security-quiz
```

Option 2: Pull pre-built image from Docker Hub
```bash
# Pull the image (replace 'yourusername/repo' with your Docker Hub details)
docker pull yourusername/security-quiz-docker

# Run the container
docker run -it organization/security-quiz-docker
```

Option 3: Use Docker image archive (.tar)
For offline distribution or when Docker Hub access is limited:
```bash
# For the distributor: Save image to a .tar file
docker build -t security-quiz .
docker save security-quiz > security-quiz.tar

# For recipients: Load the image from the .tar file
docker load < security-quiz.tar
docker run -it security-quiz
```

### Pushing to Docker Hub
To make your image available to others via Docker Hub:
```bash
# Login to Docker Hub
docker login

# Tag your image with your Docker Hub username
docker tag security-quiz yourusername/security-quiz

# Push the image to Docker Hub
docker push yourusername/security-quiz
```
Others can then pull your image using:
```bash
bashCopydocker pull yourusername/security-quiz
docker run -it yourusername/security-quiz
```
