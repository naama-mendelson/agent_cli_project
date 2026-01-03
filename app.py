import os
from dotenv import load_dotenv
from openai import OpenAI
import gradio as gr

# Load environment variables from .env
load_dotenv()

# Initialize OpenAI client with API key
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def respond(message, chat_history):
    # Send the user message to OpenAI
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "user", "content": message}
        ]
    )

    # Extract assistant's answer
    answer = response.choices[0].message.content

    # Gradio ChatInterface manages history automatically
    return answer

# Launch chat UI
gr.ChatInterface(fn=respond).launch()
