import os
from dotenv import load_dotenv
from openai import OpenAI

# טוען את משתני הסביבה (.env)
load_dotenv()

# יצירת לקוח OpenAI עם המפתח מה-ENV
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# פונקציה שמקבלת טקסט ומחזירה פקודת CLI
def natural_to_cli(text: str) -> str:
    prompt = f"""
    אתה ממיר הוראות טבעיות לפקודות CLI של Windows.
    תן רק פקודה אחת, בלי הסברים.

    הוראה:
    {text}
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message["content"]


# בדיקה
if __name__ == "__main__":
    print(natural_to_cli("תראי לי את כל הקבצים בתיקייה"))
