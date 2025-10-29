🚀 End-to-End CI/CD Pipeline using GitHub Actions, Docker & AWS EC2

This project demonstrates a complete CI/CD pipeline that automatically tests, builds, and deploys a Python web application to an AWS EC2 instance using GitHub Actions and Docker.

🧩 Project Overview

Whenever new code is pushed to the main branch:

🧪 Code Testing: Runs automated tests using pytest.

🏗️ Build & Push: Builds a Docker image and pushes it to Docker Hub.

☁️ Deploy: Connects securely to an AWS EC2 instance and deploys the updated container.

🔍 Health Check: Verifies that the application is live and running properly.

⚙️ Tech Stack

CI/CD: GitHub Actions

Containerization: Docker & Docker Hub

Cloud: AWS EC2

Language: Python (Flask app with pytest tests)

🛠️ How It Works

Code changes are pushed to the main branch.

GitHub Actions automatically:

Checks out the repo

Installs dependencies

Runs tests

Builds and tags a Docker image

Pushes the image to Docker Hub

SSHs into EC2, pulls the new image, and runs the updated container

The app is accessible on the EC2 public IP after deployment.

🔐 Secrets Used

You’ll need to configure these in your GitHub repository:

DOCKER_USERNAME

DOCKER_PASSWORD

EC2_HOST

EC2_USERNAME

EC2_SSH_KEY

📁 Key Files

.github/workflows/main.yml → GitHub Actions pipeline file

Dockerfile → Builds the Python app image

test_app.py → Test file using pytest

app.py → Simple Python web app

✅ Highlights

Full CI/CD automation from code push to deployment.

Integrated automated testing before deployment.

Versioned Docker images with SHA tagging.

Zero-downtime deployment using Docker containers.

Demonstrates real-world DevOps workflow using cloud and automation tools.

🌐 Project Flow

Push to main → GitHub Actions → Test → Build → Push to Docker Hub → Deploy to EC2 → Health Check ✅

🧠 Learning Outcome

Understanding of how CI/CD pipelines work end-to-end.

Hands-on with GitHub Actions, Docker, and AWS EC2 automation.

Real-world exposure to DevOps practices used in production systems.
