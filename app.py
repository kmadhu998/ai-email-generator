import os
from langchain.llms import OpenAI

# 🔑 Add your API key
os.environ["OPENAI_API_KEY"] = "your-api-key-here"

llm = OpenAI(temperature=0.7)

print("✉️ AI Email Generator Ready!\n")

while True:
    role = input("Enter role (HR / Manager / Team Lead): ")
    tone = input("Enter tone (formal / friendly / polite): ")
    context = input("Enter email context: ")

    prompt = f"""
    You are a professional {role}.
    Write a {tone} email reply.

    Email content:
    {context}

    Make it clear, structured, and professional.
    """

    response = llm(prompt)

    print("\n✅ Generated Email:\n")
    print(response)

    cont = input("\nDo you want to continue? (yes/no): ")
    if cont.lower() != "yes":
        break