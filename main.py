from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware
from transformers import pipeline

app = FastAPI()

# Allow frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

generator = pipeline("text-generation", model="distilgpt2")

@app.post("/generate")
async def generate_post(
    topic: str = Form(...),
    tone: str = Form(...),
    length: str = Form(...),
    prompt: str = Form(...)
):
    input_text = (
        f"Write a {tone} LinkedIn post about {topic}. "
        f"The post should be {length} in length. "
        f"Additional context: {prompt}"
    )

    result = generator(input_text, max_length=200, num_return_sequences=1)
    generated_text = result[0]["generated_text"]

    return {"generated_post": generated_text}
