import requests
import json

# Ollama API URL
url = "http://localhost:11434/api/generate"
headers = {"Content-Type": "application/json"}

# Define the sequence of AI models
model_chain = ["llama3", "llava", "gemma:2b"]

# Main interaction loop
while True:
    user_input = input("Enter your prompt (or type 'exit' to quit): ").strip()
    if user_input.lower() == "exit":
        print("Exiting...")
        break

    # This will be the input to the first model
    current_prompt = user_input
    transcript = []

    for model in model_chain:
        print(f"\n🔁 Querying model: {model}...")
        data = {
            "model": model,
            "prompt": current_prompt
        }

        try:
            response = requests.post(url, headers=headers, data=json.dumps(data))
            response.raise_for_status()

            full_response = ""
            # Each line of response is a JSON object
            for line in response.text.strip().splitlines():
                json_data = json.loads(line)
                full_response += json_data.get("response", "")

            # Save interaction to transcript
            transcript.append({
                "model": model,
                "input_prompt": current_prompt,
                "output_response": full_response.strip()
            })

            # The output becomes the next model's prompt
            current_prompt = full_response.strip()

        except Exception as e:
            print(f"❌ Error communicating with model {model}: {e}")
            break

    # Show the full communication transcript
    print("\n📜 AI Chain Transcript:")
    for step in transcript:
        print(f"\n🧠 Model: {step['model']}")
        print(f"📝 Prompt: {step['input_prompt']}")
        print(f"💬 Response: {step['output_response']}")
    print("\n✅ End of interaction\n")
