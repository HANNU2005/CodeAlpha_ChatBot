def chatbot_response(user_input):
    """
    Simple rule-based chatbot that responds to basic greetings and questions.
    Returns appropriate responses based on user input.
    """
    # Convert input to lowercase for easier matching
    user_input = user_input.lower().strip()
    # Define response rules using if-elif statements
    if user_input in ["hello", "hi", "hey", "greetings"]:
        return "Hi!"
    elif user_input in ["how are you", "how are you?", "how do you do"]:
        return "I'm fine, thanks!"
    elif user_input in ["bye", "goodbye", "see you", "farewell"]:
        return "Goodbye!"
    elif user_input in ["what's your name", "who are you", "what are you"]:
        return "I'm a simple chatbot!"
    elif user_input in ["help", "what can you do"]:
        return "I can respond to greetings, say goodbye, and answer basic questions!"
    elif "weather" in user_input:
        return "I don't have access to weather data, but I hope it's nice!"
    elif "time" in user_input:
        return "I don't have access to the current time, sorry!"
    else:
        return "I'm not sure how to respond to that. Try saying 'hello', 'how are you', or 'bye'!"
def run_chatbot():
    """
    Main function that runs the chatbot in a loop.
    Handles user input and displays responses.
    """
    print("🤖 Simple Chatbot Started!")
    print("Type 'quit' or 'exit' to stop the chatbot.\n")
    # Main conversation loop
    while True:
        # Get user input
        user_message = input("You: ")
        # Check for exit commands
        if user_message.lower() in ['quit', 'exit', 'stop']:
            print("Chatbot: Goodbye! Thanks for chatting!")
            break
        # Get chatbot response
        response = chatbot_response(user_message)
        # Display response
        print(f"Chatbot: {response}")
# Run the chatbot if this script is executed directly
if __name__ == "__main__":
    run_chatbot()