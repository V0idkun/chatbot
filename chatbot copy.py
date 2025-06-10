import spacy
import nltk
import re
# nltk.download('punkt')
# nltk.download('stopwords')
# nltk.download('wordnet')
# nltk.download('averaged_perceptron_tagger')
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import string
import streamlit as st

# nlp = spacy.load("en_core_web_md")  # or en_core_web_lg for better accuracy

# Load the text file and preprocess the data
with open('ANIME BEGINNERS.txt', 'r', encoding='utf-8') as f:
    data = f.read().replace('\n', ' ')

sections = re.split(r"\n(?=\d+\.\s)", data)
# Tokenize the text into sentences
sentences = [section.strip() for section in sections if section.strip()]
# Define a function to preprocess each sentence
def preprocess(sentence):
    # Tokenize the sentence into words
    words = word_tokenize(sentence, preserve_line=True)
    # Remove stopwords and punctuation
    words = [word.lower() for word in words if word.lower() not in stopwords.words('english') and word not in string.punctuation]
    # Lemmatize the words
    lemmatizer = WordNetLemmatizer()
    words = [lemmatizer.lemmatize(word) for word in words]
    return words

# Preprocess each sentence in the text
corpus = []

for section in sections:
    if section.strip():
        original = section.strip()
        processed = preprocess(original)
        corpus.append((original, processed))

# Define a function to find the most relevant sentence given a query
def get_most_relevant_sentence(query):
    # Preprocess the query
    query = preprocess(query)
    # Compute the similarity between the query and each sentence in the text
    max_similarity = 0
    most_relevant_sentence = ""
    for sentence in corpus:
        similarity = len(set(query).intersection(sentence)) / float(len(set(query).union(sentence)))
        if similarity > max_similarity:
            max_similarity = similarity
            most_relevant_sentence = " ".join(sentence)
    return most_relevant_sentence

def chatbot(question):
    # Find the most relevant sentence
    most_relevant_sentence = get_most_relevant_sentence(question)
    # Return the answer
    return most_relevant_sentence
# Initialize session state for chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

def main():
    st.title("Anime Chatbot")
    st.write("Hello! I'm a chatbot. I am an anime beginners guide.")
    # Get the user's question
    question = st.text_input("You:", key="input")
    submit = st.button("Submit")

    if submit and question:
        greetings = ['hi', 'hello', 'good day', 'good morning', 'good afternoon', 'good evening']
        if question.lower().strip() in greetings:
            response = "Hello! I'm your anime assistant. Ask me anything about anime!"
        else:
            response = chatbot(question)

        # Add the user input and bot response to the history
        st.session_state.chat_history.append(("You", question))
        st.session_state.chat_history.append(("Chatbot", response))

    # Display chat history
    for speaker, message in st.session_state.chat_history:
        st.write(f"**{speaker}:** {message}")
if __name__ == "__main__":
    main()














