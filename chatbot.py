import re
import random
import wikipediaapi
import wikipedia

# Define a dictionary of predefined rules and lists of responses
responses = {
    "hello": ["Hi there! How can I assist you today?", "Hello! What can I do for you?"],
    "how are you": ["I'm just a computer program, but thanks for asking!", "I'm doing well, thanks!"],
    "what is your name": ["I'm a chatbot, your friendly chatbot."],
    "goodbye": ["Goodbye! Have a great day!", "Goodbye! Don't hesitate to return if you have more questions."],
    "default": ["I'm sorry, I don't understand that. Can you please rephrase or ask another question?", "I'm not sure I follow. Can you try asking in a different way?"]
}

# Function to match user input to predefined rules
def get_response(user_input):
    user_input = user_input.lower()  # Convert input to lowercase to avoid case sensitivity

    for pattern, response_list in responses.items():
        if re.search(pattern, user_input):
            return random.choice(response_list)

    # If no predefined rule matches, return a default response
    return random.choice(responses["default"])

# Function to search Wikipedia and retrieve a summary
def search_wikipedia(query):
    try:
        summary = wikipedia.summary(query, sentences=2)
        return summary
    except wikipedia.exceptions.DisambiguationError as e:
        return "There are multiple possible topics for this query. Please specify your search."
    except wikipedia.exceptions.HTTPTimeoutError as e:
        return "Wikipedia search timed out. Please try again later."
    except wikipedia.exceptions.PageError as e:
        return "The requested page does not exist in Wikipedia."
    except Exception as e:
        return "An error occurred while searching Wikipedia. Please try again."

# Main chatbot loop 
while True:
    user_input = input("You: ")
    
    if user_input.lower() == "exit":
        print("Chatbot: Goodbye!")
        break

    if user_input.lower().startswith("search "):
        # Perform a Wikipedia search if the user starts the input with "search"
        query = user_input[len("search "):]
        result = search_wikipedia(query)
        print("Chatbot: Wikipedia Summary -", result)
    else:
        # Handle other user input with predefined responses
        response = get_response(user_input)
        print("Chatbot:", response)
