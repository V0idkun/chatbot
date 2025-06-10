import nltk
import streamlit as st
import os
os.environ['STREAMLIT_SERVER_PORT'] = '8502'
from nltk.chat.util import Chat, reflections

# Define pairs of patterns and responses
pairs = [
    [
        r"(hi|hello|hey|good morning|good afternoon|good evening)",
        ["Hello! Welcome to our bank. How can I assist you today?", "Hi there! How can I help you with your banking needs?"]
    ],
    [
        r"how are you ?",
        ["I'm just a bot, but I'm here to assist you with any banking inquiries!", "I'm doing great! How can I assist you today?"]
    ],
    [
        r"what is your name ?",
        ["I am your virtual banking assistant.", "You can call me BankBot, your personal banking assistant!"]
    ],
    [
        r"(what services do you offer|what can you do\??)",
        ["I can help you check your account balance, transfer funds, provide loan information, open a new account, and answer general banking queries."]
    ],
    [
        r"(how do I open an account\??|account opening process)",
        ["To open an account, you need to provide a valid ID, proof of address, and an initial deposit. You can visit our nearest branch or apply online through our website."]
    ],
    [
        r"(how do I check my account balance\??|check balance)",
        ["You can check your balance through our mobile app, internet banking, or by visiting the nearest ATM."]
    ],
    [
        r"(how can I transfer money\??|fund transfer)",
        ["You can transfer money using our mobile banking app, internet banking, or by visiting your nearest branch. Would you like to know the steps for online transfers?"]
    ],
    [
        r"(tell me about your loans|loan options|how to apply for a loan)",
        ["We offer various loans, including personal, home, auto, and business loans. You can apply online or visit a branch. Would you like details on a specific loan type?"]
    ],
    [
        r"(how do I reset my password\??|forgot password)",
        ["You can reset your password using the 'Forgot Password' option on our online banking portal. You will need to verify your identity before setting a new password."]
    ],
    [
        r"(what are your interest rates\??|current interest rates)",
        ["Our interest rates vary depending on the type of account or loan. Please visit our website or contact customer support for the latest rates."]
    ],
    [
        r"(what are your working hours\??|bank working hours)",
        ["Our bank operates from Monday to Friday, 9 AM to 5 PM. Some branches are open on Saturdays from 9 AM to 1 PM."]
    ],
    [
        r"(how can I contact customer support\??|customer service)",
        ["You can reach our customer support via phone at 123-456-7890, email at support@bank.com, or visit our nearest branch."]
    ],
    [
        r"(how can I update my account details\??|update personal details)",
        ["You can update your personal details by logging into online banking or visiting a branch with the required identification documents."]
    ],
    [
        r"(how secure is my account\??|account security)",
        ["Your security is our priority! We use encryption, two-factor authentication, and other security measures to protect your account. Always avoid sharing your PIN or password with anyone."]
    ],
    [
        r"(tell me a joke)",
        ["Why did the bank teller break up with the calculator? Because she felt like she was being used for her digits!"]
    ],
    [
        r"(thank you|thanks)",
        ["You're welcome! Is there anything else I can help you with?", "Happy to help! Have a great day!"]
    ],
    [
        r"(quit|exit)",
        ["Thank you for banking with us! Have a great day!", "Goodbye! Feel free to reach out anytime."]
    ],
    [
        r".*",
        ["I'm sorry, I didn't understand that. Could you please rephrase?", "Can you clarify your request? I'm here to help with banking services."]
    ]
]


# Create a Chat object
chatbot = Chat(pairs, reflections)

# Streamlit app
def main():
    st.title("Simple Chatbot")
    st.write("Welcome to the chatbot. Type something to get started!")

    # Initialize session state to store chat history
    if "history" not in st.session_state:
        st.session_state.history = []

    # Input from user
    user_input = st.text_input("You: ")

    if user_input:
        # Get chatbot response
        response = chatbot.respond(user_input)
        st.session_state.history.append(f"You: {user_input}")
        st.session_state.history.append(f"ChatBot: {response}")

    # Display chat history
    for message in st.session_state.history:
        st.write(message)

if __name__ == "__main__":
    main()