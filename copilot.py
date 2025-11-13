from openai import OpenAI
client = OpenAI(
    base_url="http://192.168.0.106:1234/v1",
    api_key="lm-studio" 
)
model_name = "qwen/qwen3-4b-thinking-2507"
  # You can change to another if you prefer

system_prompt = "You are a smart and friendly AI copilot. Help the user with code, reasoning, and tasks."

print("🤖Copilot is ready ! Type your message ")

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        print("Copilot: Goodbye 👋")
        break

    response = client.chat.completions.create(
        model=model_name,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_input}
        ]
    )

    print("Copilot:", response.choices[0].message.content.strip(), "\n")
