from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import os

from app.database import save_user, save_plan, update_plan, get_original_plan, SessionLocal, User, WorkoutPlan
from app.gemini_generator import generate_workout_gemini
from app.gemini_flash_generator import generate_nutrition_tip_with_flash
from app.updated_plan import update_workout_plan

app = FastAPI()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_DIR = os.path.join(os.path.dirname(BASE_DIR), "templates")
templates = Jinja2Templates(directory=TEMPLATE_DIR)

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/generate-workout", response_class=HTMLResponse)
async def generate_workout(
    request: Request, user_id: int = Form(...), username: str = Form(...), 
    age: int = Form(...), weight: float = Form(...), 
    goal: str = Form(...), intensity: str = Form(...)
):
    save_user(user_id, username, age, weight, goal, intensity)
    
    workout_plan = generate_workout_gemini({"goal": goal, "intensity": intensity})
    save_plan(user_id, workout_plan)
    
    nutrition_tip = generate_nutrition_tip_with_flash(goal)
    
    return templates.TemplateResponse("result.html", {
        "request": request, "username": username, "user_id": user_id, 
        "goal": goal, "intensity": intensity, "workout_plan": workout_plan, 
        "nutrition_tip": nutrition_tip, "message": "Plan Generated Successfully!"
    })

@app.post("/submit-feedback", response_class=HTMLResponse)
async def submit_feedback(request: Request, user_id: int = Form(...), feedback: str = Form(...)):
    original_plan = get_original_plan(user_id)
    if not original_plan:
        return HTMLResponse("<h1>Error: User plan not found!</h1>")
    
    updated = update_workout_plan(original_plan, feedback)
    update_plan(user_id, updated)
    
    return templates.TemplateResponse("result.html", {
        "request": request, "workout_plan": updated, "message": "Plan Updated Successfully based on your feedback!"
    })

@app.get("/view-all-users", response_class=HTMLResponse)
async def view_all_users(request: Request):
    db = SessionLocal()
    users = db.query(User).all()
    user_data = []
    for user in users:
        plan = db.query(WorkoutPlan).filter(WorkoutPlan.user_id == user.id).first()
        user_data.append({
            "id": user.id, "name": user.name, "age": user.age, "weight": user.weight,
            "goal": user.goal, "intensity": user.intensity,
            "original_plan": plan.original_plan if plan else "N/A",
            "updated_plan": plan.updated_plan if plan and plan.updated_plan else "Not updated"
        })
    db.close()
    return templates.TemplateResponse("all_users.html", {"request": request, "users": user_data})