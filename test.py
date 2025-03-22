
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

def chatbot():
    # Load the pre-trained model and tokenizer
    model_name = "microsoft/DialoGPT-medium"  # You can use other models like "gpt2"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)

    # Chatbot loop
    print("Chatbot: Hi! I am your chatbot. Type 'exit' to end the conversation.")
    chat_history_ids = None

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Chatbot: Goodbye!")
            break

        # Encode user input and append to chat history
        new_input_ids = tokenizer.encode(user_input + tokenizer.eos_token, return_tensors="pt")
        chat_history_ids = (
            new_input_ids if chat_history_ids is None else torch.cat([chat_history_ids, new_input_ids], dim=-1)
        )

        # Generate a response
        response_ids = model.generate(chat_history_ids, max_length=1000, pad_token_id=tokenizer.eos_token_id)
        response = tokenizer.decode(response_ids[:, chat_history_ids.shape[-1]:][0], skip_special_tokens=True)

        print(f"Chatbot: {response}")

def main():
    chatbot()

if __name__ == "__main__":
    main()
    