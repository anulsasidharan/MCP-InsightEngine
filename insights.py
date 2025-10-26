import os
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Method for 
def get_llm_insights(prompt):
    response = client.chat.completions.create(
        model = "gpt-4o-mini",
        messages = [
            {"role":"system", "content":"you are a helpful system agent analyze my data and give me a response"},
            {"role":"user","content":prompt}
        ],
        temperature=0.3 # Set low to avoid hallucination
    ) # type: ignore
    return response.choices[0].message.content