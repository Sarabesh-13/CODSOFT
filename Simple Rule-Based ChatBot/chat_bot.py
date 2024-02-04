#Simple Rule Based ChatBot

def rule_based_response(user_input):
    if "hello" in user_input.lower():
        return "Hello! How can I help you today?"
    elif "goodbye" in user_input.lower():
        return "Goodbye! Have a great day."
    elif "how are you" in user_input.lower():
        return "I'm just a computer program, but thanks for asking!"
    elif "your name" in user_input.lower():
        return "I don't have a name, but you can call me Chatbot."
    elif "what's your name" in user_input.lower():
        return "I don't have a name, but you can call me Chatbot."
    elif "help" in user_input.lower():
        return "Sure, I'm here to help. What do you need assistance with?"
    else:
        return "I'm sorry, I didn't understand that. Can you please rephrase or ask another question?"

def chatbot():
    print("Rule-based Chatbot: Type 'exit' to end the conversation.")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() == 'exit' or user_input.lower() == 'quit':
            print("Chatbot: Goodbye!")
            break
        elif user_input.lower() == 'ok' or user_input.lower() == 'okay':
            print("Chatbot: Bye!")
            break

        # Rule-based response
        response = rule_based_response(user_input)
        
        if response:
            print("Chatbot:", response)


a=chatbot()
