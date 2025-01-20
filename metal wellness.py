import random

# Function to analyze sentiment based on keywords
def analyze_sentiment(user_message):
    """Basic sentiment analysis based on keywords."""
    # Convert message to lowercase for case insensitive comparison
    message = user_message.lower()

    # Define keywords for different sentiments
    positive_keywords = ['happy', 'good', 'great', 'excited', 'joyful', 'positive']
    negative_keywords = ['sad', 'angry', 'stressed', 'down', 'anxious', 'bad', 'tired']
    neutral_keywords = ['okay', 'fine', 'neutral', 'average']

    # Sentiment detection based on keywords
    if any(word in message for word in positive_keywords):
        return "positive"
    elif any(word in message for word in negative_keywords):
        return "negative"
    elif any(word in message for word in neutral_keywords):
        return "neutral"
    else:
        return "neutral"  # Default sentiment

# Function to provide wellness tips based on sentiment
def wellness_tips(sentiment):
    """Provide wellness tips based on sentiment."""
    if sentiment == "positive":
        tips = [
            "Keep up the great work! Stay motivated and try something new today.",
            "It’s amazing that you’re feeling great! Perhaps try something creative like drawing or writing."
        ]
    elif sentiment == "negative":
        tips = [
            "I'm sorry you're feeling this way. Try a few minutes of deep breathing or take a walk outside.",
            "It's okay to feel down. Let’s try a mindfulness exercise together."
        ]
    else:
        tips = [
            "It’s normal to feel neutral sometimes. Try listening to some relaxing music or journaling.",
            "Why not take a break and try something new to refresh yourself?"
        ]
    
    return random.choice(tips)

# Function to handle user input and provide responses
def chatbot():
    print("Welcome to the Student Mental Wellness Platform!")
    print("I’m here to listen and provide support. Please share how you’re feeling today.")
    
    while True:
        user_message = input("You: ")

        # Exit condition
        if user_message.lower() in ["exit", "quit", "bye"]:
            print("Goodbye! Remember to take care of your mental health. Take care!")
            break

        # Analyze sentiment from user message
        sentiment = analyze_sentiment(user_message)
        wellness_advice = wellness_tips(sentiment)

        # Display wellness advice
        print(f"Chatbot: {wellness_advice}")
        
        # Handle emergency escalation
        if "help" in user_message.lower() or "emergency" in user_message.lower():
            print("Chatbot: It sounds like you may need immediate support. Please contact a counselor or a trusted person.")
            break
        
        # Continue interaction
        print("Chatbot: How else are you feeling? Or if you want to exit, type 'exit'.")

# Run the chatbot
if __name__ == "__main__":
    chatbot()
