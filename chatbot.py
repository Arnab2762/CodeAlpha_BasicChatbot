def get_response(user_input):
    """Return a predefined reply based on the user's message."""
    message = user_input.lower().strip()

    if message == "hello":
        return "Hi!"
    elif message == "how are you":
        return "I'm fine, thanks!"
    elif message == "bye":
        return "Goodbye!"
    else:
        return "Sorry, I didn't understand that. Try 'hello', 'how are you' or 'bye'."


def main():
    print("Chatbot: Hello! Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        reply = get_response(user_input)
        print("Chatbot:", reply)
        if user_input.lower().strip() == "bye":
            break


if __name__ == "__main__":
    main()