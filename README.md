# 🧠 ChatterMind – A Rule-Based Chatbot using Python & NLTK

Welcome to **ChatterMind**, a simple yet smart chatbot built using **Python** and the **Natural Language Toolkit (NLTK)**.  

This chatbot uses **regular expressions** and **pattern–response pairs** to simulate human-like conversations.  

It’s a beginner-friendly project that helps you understand:
- Basics of **Natural Language Processing (NLP)**
- How **rule-based chatbots** work
- Using **NLTK’s `Chat` class** for dialogue systems

---

## 🚀 Features

✅ Predefined conversational patterns  
✅ Built-in **reflections** for human-like responses  
✅ Handles greetings, emotions, jokes, and even tech questions  
✅ Fully commented and easy to understand  
✅ Runs directly in your terminal — lightweight and fun

---

## 🧩 Technologies Used

- **Python **
- **NLTK (Natural Language Toolkit)**
- **Regular Expressions (re module)**

---

## 🧠 How It Works

ChatterMind is built on **pattern–response pairs** that look like this:
```python
pairs = [
    [r"hi|hello|hey", ["Hello! How can I help you today?", "Hi there! How may I assist you?"]],
    [r"my name is (.*)", ["Hello %1! How can I assist you today?"]],
    [r"tell me a joke", ["Why don’t skeletons fight each other? They don’t have the guts!"]],
    [r"bye|exit", ["Goodbye! Have a great day!", "See you later!"]],
]
