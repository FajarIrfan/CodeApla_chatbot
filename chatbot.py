import spacy
import random

# Load spaCy NLP model
nlp = spacy.load("en_core_web_sm")

# Define chatbot responses
responses = {
    "greeting": ["Hello! How can I assist you today?", "Hey there! Need any help?", "Hi! What’s up?"],
    "goodbye": ["Goodbye! Have a great day!", "See you later!", "Bye! Take care."],
    "how_are_you": ["I'm just a bot, but I'm doing great! How about you?", "I'm fine! What about you?"],
    "name": ["I'm a chatbot created by Fajar Irfan.", "You can call me ChatBot."],
    "weather": ["I'm not a weather bot, but you can check an app for real-time updates!", "I can't predict the weather, but I hope it's nice where you are!"],
    "time": ["I don't have a clock, but you can check your device!", "Time is an illusion, but you can check it on your phone!"],
    "age": ["I'm a bot, so I don't age, but I'm always learning!", "I'm timeless! What about you?"],
    "hobby": ["I love chatting with people like you!", "My favorite hobby is learning new things!"],
    "food": ["I don’t eat, but I hear pizza is amazing!", "Food sounds great! What’s your favorite dish?"],
    "sports": ["I’m not into sports, but I hear football is fun!", "Do you like playing sports?"],
    "movie": ["I don't watch movies, but I'd love to hear about your favorites!", "Tell me about a movie you like!"],
    "book": ["Books are great! What’s your favorite?", "I love books, but I don’t have hands to hold them!"],
    "joke": ["Why don’t skeletons fight each other? They don’t have the guts!", "Why did the scarecrow win an award? Because he was outstanding in his field!"],
    "advice": ["Always keep learning!", "Stay positive and keep moving forward!"],
    "motivation": ["You can achieve anything with hard work and determination!", "Keep going! Success is just around the corner!"],
    "unknown": ["That's interesting! Tell me more.", "I'm not sure, but I’d love to learn more.", "Could you explain that differently?"]
}

# Function to determine intent
def get_intent(user_input):
    doc = nlp(user_input.lower())

    for token in doc:
        if token.lemma_ in ["hello", "hi", "hey"]:
            return "greeting"
        elif token.lemma_ in ["bye", "goodbye", "see you"]:
            return "goodbye"
        elif "name" in user_input.lower():
            return "name"
        elif "how" in user_input.lower() and "you" in user_input.lower():
            return "how_are_you"
        elif "weather" in user_input.lower():
            return "weather"
        elif "time" in user_input.lower():
            return "time"
        elif "age" in user_input.lower():
            return "age"
        elif "hobby" in user_input.lower():
            return "hobby"
        elif "food" in user_input.lower():
            return "food"
        elif "sports" in user_input.lower():
            return "sports"
        elif "movie" in user_input.lower():
            return "movie"
        elif "book" in user_input.lower():
            return "book"
        elif "joke" in user_input.lower():
            return "joke"
        elif "advice" in user_input.lower():
            return "advice"
        elif "motivation" in user_input.lower():
            return "motivation"

    return "unknown"

# Chat function
def chatbot():
    print("Hello! I'm an improved chatbot. Type 'bye' to exit.")

    while True:
        user_input = input("You: ")
        if user_input.lower() in ['bye', 'exit', 'quit']:
            print("ChatBot: Goodbye! Have a nice day!")
            break

        intent = get_intent(user_input)
        response = random.choice(responses[intent])
        print("ChatBot:", response)

if __name__ == "__main__":
    chatbot()
