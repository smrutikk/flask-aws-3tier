
# 🧩 Three-Tier Web Application using Flask, MySQL, and AWS

## 🚀 Overview
This project demonstrates the deployment of a **3-Tier Architecture Web Application** on **Amazon Web Services (AWS)** using **Flask (Python)** as the backend, **MySQL (RDS)** as the database, and **HTML/CSS (S3)** as the frontend presentation layer.

The project simulates a **Student Management System** where users can **add, view, and delete student records** through a simple web interface.

---

## 🏗️ Architecture
The project follows the standard **Three-Tier Architecture** pattern:

| Layer | Service | Description |
|-------|----------|-------------|
| **Presentation Layer** | Amazon S3 / Flask Templates | Hosts the frontend UI for users |
| **Application Layer** | Amazon EC2 (Flask App) | Handles business logic and routes user requests |
| **Database Layer** | Amazon RDS (MySQL) | Stores persistent student data |

---

## ⚙️ Tech Stack

| Category | Technology |
|-----------|-------------|
| **Frontend** | HTML, CSS |
| **Backend** | Python (Flask) |
| **Database** | MySQL (on AWS RDS) |
| **Cloud** | AWS EC2, S3, RDS |
| **Version Control** | Git + GitHub |

---

## 💡 Use Case
**Student Management Web App**

This app allows users to:
- ➕ Add new students
- 📋 View all student records
- ❌ Delete existing student records

Each record contains:
- `ID`
- `Name`
- `Email`

---

## 🧠 Implementation Phases

### 🧩 Phase 1 — Project Planning
- Defined use case and architecture.
- Selected appropriate AWS services (EC2, S3, RDS).
- Designed database schema for MySQL (students table).

### ⚙️ Phase 2 — Database Layer
- Created **Amazon RDS (MySQL)** instance.
- Configured inbound rules in Security Groups for connectivity.
- Tested connection from local Flask app using MySQL connector.


### 🧩 Phase 3 — Application Layer
- Set up **EC2 Ubuntu Instance**.
- Installed Python, Flask, and required dependencies.
- Created virtual environment (`python3 -m venv venv`).
- Deployed the Flask backend (`app.py`) to handle student data CRUD operations.
- Configured inbound rules for port 5000 and 80 (HTTP).


### 🌐 Phase 4 — Presentation Layer
- Hosted static frontend (HTML, CSS) on **Amazon S3**.
- Configured public access and bucket policies.
- Linked S3 frontend to Flask API endpoint (EC2 public DNS).
- Tested full data flow (Frontend → Backend → Database).


---

## 📸 Screenshots
Add screenshots in your GitHub repo like this:

![Architecture Diagram](screenshots/architecture.png)
![RDS Setup](screenshots/rds.png)
![Flask App](screenshots/flask.png)
![S3 Bucket](screenshots/s3.png)
![Final Output](screenshots/app_output.png)

---


