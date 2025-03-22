from transformers import pipeline

class Chatbot:
    def __init__(self):
        self.model = pipeline("conversational", model="microsoft/DialoGPT-medium")

    def get_response(self, user_input):
        response = self.model(user_input)
        return response[0]['generated_text']

def main():
    chatbot = Chatbot()
    print("Chatbot is ready! Type 'exit' to stop.")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye!")
            break
        response = chatbot.get_response(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    main()