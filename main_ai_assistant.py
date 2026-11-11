import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(
    base_url=os.getenv("BASE_URL"),
    api_key=os.getenv("API_KEY")
)

messages=[]

# messages.append(
#     {
#         "role": "system", 
#         "content": "Act as a humble and helpful assistant. Always respond in a concise manner within 50 words"
#     }
# )
while True:
    user_input = input("\nYou: ")
    
    if user_input.lower() in ["exit", "quit", "bye", "goodbye"]:
        print("Exiting the assistant. Goodbye!")
        break
    
    messages.append(
        {
            "role": "user", 
            "content": user_input
        }
    )
    response = client.chat.completions.create(
        model=os.getenv("MODEL"),
        messages=messages
    )
    messages.append(
        {
            "role": "assistant",
            "content": response.choices[0].message.content
        }
    )
    print("Assistant: ", response.choices[0].message.content)
    print("\n\n\n")
    # print("Assistant: ", response.choices[0].message.role)
