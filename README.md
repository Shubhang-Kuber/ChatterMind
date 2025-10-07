# ChatterMind – A Rule-Based Chatbot using Python & NLTK

Welcome to **ChatterMind**, a simple and smart chatbot built using **Python** and the **Natural Language Toolkit (NLTK)**.

This chatbot uses **regular expressions** and **pattern–response pairs** to simulate human-like conversations.

This project is beginner-friendly and demonstrates:
- Basics of **Natural Language Processing (NLP)**
- How **rule-based chatbots** operate
- Usage of **NLTK’s `Chat` class** for building dialogue systems

---

## Features

- Predefined conversational patterns
- Built-in **reflections** for human-like responses
- Handles greetings, emotions, jokes, and technical questions
- Fully commented code for easy understanding
- Lightweight and runs directly in the terminal

---

## Technologies Used

- **Python**
- **NLTK (Natural Language Toolkit)**
- **Regular Expressions (re module)**

---

## How It Works

ChatterMind operates using **pattern–response pairs**. Example:

```python
pairs = [
    [r"hi|hello|hey", ["Hello! How can I help you today?", "Hi there! How may I assist you?"]],
    [r"my name is (.*)", ["Hello %1! How can I assist you today?"]],
    [r"tell me a joke", ["Why don’t skeletons fight each other? They don’t have the guts!"]],
    [r"bye|exit", ["Goodbye! Have a great day!", "See you later!"]],
]
