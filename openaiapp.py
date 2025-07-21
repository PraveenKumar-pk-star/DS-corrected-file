! pip install openai
from openai import OpenAI
from getpass import getpass
open_ai_key=getpass("Enter the keya:")
client=OpenAI(api_key=open_ai_key)
response=client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{
        "role":"user",
        "content":"bed time story 2 lines"
    }]

)

response.choices[0].message.content
