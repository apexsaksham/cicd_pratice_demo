#  End-to-End CI/CD Pipeline (GitHub Actions · Docker · AWS EC2)

This project shows how a **simple Python web app** can be **automatically tested, built, and deployed** to an AWS EC2 server using a **real-world CI/CD pipeline**.

In short: **push code → pipeline runs → app updates by itself**.

---

## 🧩 What This Project Does

Whenever code is pushed to the **main** branch:                --

* 🧪 **Tests the code** using `pytest`
* 🏗️ **Builds a Docker image** of the app
* 📦 **Pushes the image** to Docker Hub
* ☁️ **Deploys the app** on AWS EC2
* 🔍 **Checks app health** to confirm it’s running

No manual work. No server login needed.

---

## ⚙️ Tech Stack (Simple View)

* **CI/CD:** GitHub Actions (automation engine)
* **Containers:** Docker & Docker Hub
* **Cloud Server:** AWS EC2
* **App:** Python (Flask) + pytest

---

## 🛠️ How It Works (Step by Step)

1. Developer pushes code to GitHub (`main` branch)
2. GitHub Actions pipeline starts automatically
3. Pipeline performs the following steps:

   * Downloads the code
   * Installs dependencies
   * Runs automated tests
   * Builds and tags a Docker image
   * Pushes the image to Docker Hub
   * Connects to EC2 using SSH
   * Pulls the latest image and runs the container
4. Application becomes live on the EC2 public IP

---

## 🔐 Secrets Used (For Security)

These are stored safely in GitHub Secrets:

* `DOCKER_USERNAME` – Docker Hub username
* `DOCKER_PASSWORD` – Docker Hub access token
* `EC2_HOST` – EC2 public IP or DNS
* `EC2_USERNAME` – Linux user (e.g. ec2-user)
* `EC2_SSH_KEY` – EC2 private SSH key (.pem)

No secrets are hardcoded.

---

## 📁 Important Files

* `.github/workflows/main.yml` → CI/CD pipeline definition
* `Dockerfile` → Builds the app image
* `app.py` → Python web application
* `test_app.py` → Automated tests using pytest

---

## ✅ Why This Project Is Strong

* Fully **automated CI/CD pipeline**
* Tests run **before deployment** (safe releases)
* Docker images are **versioned**
* Old containers are replaced automatically
* Uses **real DevOps tools** used in production

---

## 🌐 Pipeline Flow (Easy to Remember)

`Push Code → Test → Build → Push Image → Deploy → Health Check ✅`

---

## 🧠 What I Learned

* How CI/CD pipelines work from start to end
* How GitHub Actions automates real deployments
* How Docker simplifies app delivery
* How cloud servers (EC2) run production apps
* How DevOps removes manual deployment work

---

This project focuses on **clarity, automation, and reliability**, not fancy UI — exactly how real DevOps systems work.
