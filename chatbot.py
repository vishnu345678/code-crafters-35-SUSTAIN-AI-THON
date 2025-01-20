import requests
import json

# Define the API endpoint for bolt.new AI chatbot
BOLT_NEW_API_URL = "https://api.bolt.new/v1/chatbot"

# Function to send a message to the Bolt.new API and get a response
def get_chatbot_response(user_message):
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer YOUR_BOLT_NEW_API_KEY"  # Replace with your actual API key
    }

    payload = {
        "message": user_message,
        "context": {
            "user": "student",  # Identifier for the user (can be dynamic, based on logged-in user)
            "intent": "mental_health_assistance",  # Intent for the chatbot
        }
    }

    # Send the POST request to Bolt.new API
    try:
        response = requests.post(BOLT_NEW_API_URL, headers=headers, json=payload)
        if response.status_code == 200:
            response_data = response.json()
            return response_data['response']
        else:
            return "Sorry, I couldn't understand that. Can you please rephrase?"
    except Exception as e:
        print(f"Error: {e}")
        return "Sorry, something went wrong. Please try again later."

# Function to analyze sentiment of user input
def analyze_sentiment(user_message):
    # For simplicity, we assume the sentiment is derived from the message
    # You can integrate with bolt.new's NLP models or use a library like TextBlob for sentiment analysis
    if "happy" in user_message or "good" in user_message:
        return "positive"
    elif "sad" in user_message or "stressed" in user_message:
        return "negative"
    else:
        return "neutral"

# Function to provide wellness recommendation based on sentiment
def wellness_recommendation(sentiment):
    if sentiment == "positive":
        return "That's great to hear! Keep doing what makes you happy, maybe try something new today."
    elif sentiment == "negative":
        return "I'm sorry you're feeling that way. Try taking a few deep breaths, or let me suggest a quick relaxation exercise."
    else:
        return "It seems like you're in a neutral mood. How about doing a small act of kindness or listening to some relaxing music?"

# Main loop to simulate chatbot interaction
def chat():
    print("Hello! I'm here to help you with your mental wellness. How are you feeling today?")
    
    while True:
        user_message = input("You: ")

        # Exit condition
        if user_message.lower() in ["exit", "quit", "bye"]:
            print("Goodbye! Take care!")
            break

        # Analyze sentiment of user input
        sentiment = analyze_sentiment(user_message)

        # Get wellness recommendation based on sentiment
        wellness_advice = wellness_recommendation(sentiment)
        print(f"Chatbot: {wellness_advice}")

        # Get chatbot's response to user input
        chatbot_response = get_chatbot_response(user_message)
        print(f"Chatbot: {chatbot_response}")

        # Emergency escalation (this can be customized based on the use case)
        if "help" in user_message or "emergency" in user_message:
            print("Chatbot: It seems you're in distress. Please contact a counselor immediately, or dial your emergency number.")

# Run the chatbot
if __name__ == "__main__":
    chat()
