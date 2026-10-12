# Flask DevOps Application

A Flask web application containerized with Docker, with automated testing using pytest and Continuous Integration (CI) using GitHub Actions.

## Features

* **Flask:** Python-based web application.
* **Docker:** Containerizes the application for consistent execution across environments.
* **Pytest:** Runs automated tests to verify application functionality.
* **GitHub Actions:** Automatically runs tests when code is pushed or a pull request is created.
* **CI/CD foundation:** Structured to support automated Docker image builds and future deployment automation.

## Tech Stack

* Python 3.10
* Flask
* Docker
* Pytest
* Git and GitHub
* GitHub Actions

## Project Structure

```text
flask-devops-app/
├── .github/
│   └── workflows/
│       └── ci.yml
├── tests/
│   └── test_app.py
├── app.py
├── Dockerfile
├── requirements.txt
├── .gitignore
└── README.md
```

## Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/YogeshPanche6301/flask-devops-app.git
cd flask-devops-app
```

### 2. Create and activate a virtual environment

Windows PowerShell:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
python app.py
```

Open the local URL displayed in your terminal.

## Run Automated Tests

Run the test suite with:

```bash
python -m pytest -v
```

## Run with Docker

Build the Docker image:

```bash
docker build -t flask-devops-app .
```

Run the container:

```bash
docker run -p 5000:5000 flask-devops-app
```

Open `http://localhost:5000` if the application listens on port 5000 inside the container.

## Continuous Integration

GitHub Actions is configured to run automated tests on pushes and pull requests. The workflow helps detect errors before changes are merged.

The next improvement is to automate Docker image builds through GitHub Actions.

## Future Improvements

* Automated Docker image builds.
* Publish versioned images to Docker Hub.
* Add code quality checks and test coverage.
* Deploy the application to a cloud platform.

## Learning Objectives

This project demonstrates practical experience with Python web applications, containerization, automated testing, Git version control, and CI pipeline automation.
