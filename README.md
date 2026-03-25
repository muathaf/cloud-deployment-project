# Automated Cloud Deployment Pipeline ☁️🚀

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-00a393.svg)
![Docker](https://img.shields.io/badge/Docker-Ready-2496ED.svg)
![CI/CD](https://img.shields.io/badge/CI%2FCD-GitHub_Actions-2088FF.svg)

## Overview
This repository contains a production-ready **FastAPI application** packaged within a **Docker container** and deployed via an automated **CI/CD pipeline using GitHub Actions**. 

This project was built to demonstrate modern Cloud Engineering and DevOps practices, specifically focusing on bridging the gap between local application development and highly available cloud infrastructure.

## 🏗️ Architecture & Tech Stack
* **Application Framework:** Python / FastAPI
* **Containerization:** Docker
* **CI/CD Orchestration:** GitHub Actions
* **Target Infrastructure:** AWS EC2 (Linux)

## ⚙️ How the Pipeline Works
This repository implements continuous integration and deployment principles:
1. **Push:** Code updates are pushed to the `main` branch.
2. **Build:** GitHub Actions automatically triggers a runner to build the new Docker image.
3. **Deploy:** The pipeline authenticates securely with the cloud server, pulls the latest container image, and seamlessly restarts the application without manual intervention.

## 🚀 Running it Locally
If you want to spin this up on your local machine, ensure you have Docker installed and run the following commands:

```bash
# Clone the repository
git clone [https://github.com/muathaf/cloud-deployment-project.git](https://github.com/muathaf/cloud-deployment-project.git)
cd cloud-deployment-project

# Build the Docker image
docker build -t cloud-app .

# Run the container
docker run -p 8000:8000 cloud-app
