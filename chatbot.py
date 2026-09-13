responses = {
    'hello': 'Hi there! Welcome to DecodeLabs AI support.',
    'how are you': 'I am operating at full structural capacity!',
    'what is your name': 'I am your rule-based AI assistant.',
    'help': 'I can respond to greetings, project info, and exit commands.',
    'bye': 'Goodbye! Have a great day.'
}

print("AI Chatbot Initialized. Type 'exit' to quit.")

while True:
    raw_input_text = input('You: ')
    clean_input = raw_input_text.lower().strip()
    
    if clean_input == 'exit':
        print("Bot: Shutting down logic engine. Goodbye!")
        break
        
    reply = responses.get(clean_input, 'I do not understand. Please try another command.')
    print(f"Bot: {reply}")