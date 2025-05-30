from openai import OpenAI
import os
from systemPrompts import getPrompts

greeting_response=[
    ""
]

def getResponse(persona:str, message:str):
    # if message == "hey":
    #     return("")
    

    API_KEY = os.getenv("API_KEY")

    client = OpenAI(api_key=API_KEY, 
    # base_url="https://api.perplexity.ai"
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
    )

    systemPrompt = getPrompts(persona)

    chat_messages = [{"role": "system", "content": systemPrompt}] + message

    response = client.chat.completions.create(
        # model="sonar-pro",
        model="gemini-2.0-flash",
        # messages=[
        #     {"role":"system", "content":systemPrompt},
        #     {"role":"user", "content":message}
        # ],
        messages=chat_messages,
        max_tokens=150,
    )

    print(response.choices[0].message)
    return(response.choices[0].message.content)
    


