# FitBuddy - AI Personal Trainer 🏋️‍♂️🤖
**Project Name:** FitBuddy - AI Fitness Plan Generator using Gemini Models 
**Team ID:** FYBTech8

FitBuddy is a dynamic, AI-powered web application that acts as a virtual personal trainer. By taking in a user's physical metrics (age, weight) and specific fitness objectives, it instantly generates a highly customized 7-day workout protocol and daily nutrition tip.

## 👥 The Team
* **Yash** - Lead Developer (Backend Architecture & AI Integration)
* **Pranali Yadav** - UI/UX Design & Frontend Parsing
* **Swaranjali Pisal** - Requirement Analysis & Database Schema
* **Vedant Shirale** - Quality Assurance & Agile Documentation

## 🚀 Tech Stack
* **Frontend:** HTML5, CSS3 (Glassmorphism), JavaScript (`marked.js`)
* **Backend:** Python 3.x, FastAPI, Uvicorn (ASGI)
* **Database:** SQLite with SQLAlchemy ORM
* **Artificial Intelligence:** Google Gemini 2.5 Flash API

## ✨ Core Features
1. **Dynamic Generation:** Creates customized 7-day routines in under 5 seconds.
2. **The Feedback Loop:** Users can submit text feedback (e.g., "Make this bodyweight only") to instantly regenerate and update their saved protocol.
3. **Session Continuity:** SQLite database securely stores user IDs, original plans, and updated plans.
4. **Admin Terminal:** A secure dashboard to view all registered clients and their AI fitness journeys.

## 💻 How to Run Locally
1. Clone the repository to your local machine.
2. Activate your virtual environment: `fitbuddy-env\Scripts\activate.bat`
3. Install dependencies: `pip install -r requirements.txt`
4. Start the server: `uvicorn app.main:app --reload`

5. Open your browser and navigate to `http://127.0.0.1:8000`
