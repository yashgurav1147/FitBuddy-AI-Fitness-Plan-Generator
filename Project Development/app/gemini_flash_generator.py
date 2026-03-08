import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel('gemini-2.5-flash')

def generate_nutrition_tip_with_flash(goal: str) -> str:
    prompt = f"Give one clear, helpful nutrition or recovery tip for someone focused on '{goal}'. The tip should be practical, friendly, and easy to understand."
    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"Error generating tip: {e}"