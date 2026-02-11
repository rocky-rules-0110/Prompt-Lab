import os
from openai import OpenAI
import config

client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=config.GROQ_API_KEY
)

def get_ai_response(prompt, temperature):
    """Sends a prompt to the AI and returns the response."""
    response = client.chat.completions.create(
        model="llama3-8b-8192", 
        messages=[{"role": "user", "content": prompt}],
        temperature=temperature,
    )
    return response.choices[0].message.content

def main():
    print("--- Welcome to the Prompt Lab ---")
    
    print("\n[Part 1: Temperature Testing]")
    user_prompt = input("Enter a creative prompt (e.g., 'Describe a city on Mars'): ")
    
    temps = [0.1, 0.5, 0.9]
    for t in temps:
        print(f"\n--- Output at Temperature {t} ---")
        print(get_ai_response(user_prompt, t))

    print("\n[Part 2: Instruction-Based Prompt Testing]")
    topic = input("Choose a topic (e.g., 'Climate Change'): ")
    
    instructions = {
        "Summary": f"Provide a brief summary of {topic}.",
        "Simplified": f"Give a simplified explanation of {topic} for a 5-year-old.",
        "Pro-Con": f"Provide a pro-con list for {topic}.",
        "Headline": f"Write a creative news headline from the year 2050 about {topic}."
    }
    
    for key, prompt in instructions.items():
        print(f"\n--- Format: {key} ---")
        print(get_ai_response(prompt, 0.7)) 
    print("\n[Part 3: Combine Both]")
    custom_prompt = input("Enter a custom instruction-based prompt: ")
    custom_temp = float(input("Choose a custom temperature (0.0 to 1.0): "))
    
    print(f"\n--- Custom Result (Temp: {custom_temp}) ---")
    print(get_ai_response(custom_prompt, custom_temp))

if __name__ == "__main__":
    main()