from openai import OpenAI
import os
from systemPrompts import getPrompts

def getResponse(persona:str, message:str):
    API_KEY = os.getenv("API_KEY")

    client = OpenAI(api_key=API_KEY, base_url="https://api.perplexity.ai")

    systemPrompt = getPrompts(persona)

    chat_messages = [{"role": "system", "content": systemPrompt}] + message

    response = client.chat.completions.create(
        model="sonar",
        # messages=[
        #     {"role":"system", "content":systemPrompt},
        #     {"role":"user", "content":message}
        # ],
        messages=chat_messages,
        max_tokens=150
    )

    print(response.choices[0].message.content)
    return(response.choices[0].message.content)
    


