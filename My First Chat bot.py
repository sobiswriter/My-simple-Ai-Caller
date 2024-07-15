#This is where it all begun
responses = {
    "hey": "Yu Huu",
    "hi": "Hey",
    "hello": "Hi there!",
    "how are you": "I'm a bot, so I don't have feelings, but I'm functioning well!",
    "what's your name": "You can call me Chatbot.",
    "bye": "Goodbye! Have a nice day.",
    "default": "I'm not sure I understand. Could you rephrase that?"
}

def get_response(user_input):
    user_input = user_input.lower() # Make the input lowercase for easier matching
    for key, value in responses.items():
        if key in user_input:
            return value
    return responses["default"]

while True:
    user_input = input("You: ")
    response = get_response(user_input)
    print(f"Chatbot: {response}")
    if response == responses["bye"]:
        break
