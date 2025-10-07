#Step-1
#It is a python toolkit that is used for text processing and linguistic processes
#NLTK - Natural Language Toolkit
!pip install nltk


#Step-2
#re is used for the regular expressions which help in matching patterns in user input.
#chat is a class from NLTK used to build rule-based chatbots.
#reflections help make the conversion from different persons easier(1st -> 3rd, 2nd -> 3rd)
import nltk
import re
from nltk.chat.util import Chat, reflections


#Step-3
#punkt is used for tokenization.It helps in breaking down text into words or sentences
#averaged_perceptron_tagger helps to identify the grammatical parts of speech in a sentence
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')


#Step-4
pairs = [
    # --- Greetings & Introductions ---
    [r"good morning", ["Good morning! Hope you have a productive day ahead!", "Morning sunshine! What’s on your mind today?"]],
    [r"good afternoon", ["Good afternoon! How’s your day going so far?", "Hey there! Having a chill afternoon?"]],
    [r"good evening", ["Good evening! How’s everything going?", "Evening vibes! What’s up?"]],
    [r"what's up", ["Not much, just chatting with cool people like you!", "All good here. What’s up with you?"]],
    [r"howdy", ["Howdy partner! Ready to code or chill?", "Hey hey! Howdy to you too!"]],
    [r"nice to meet you", ["Nice to meet you too!", "Likewise! Always good meeting new humans."]],
    [r"where are you from", ["I live in the cloud — no rent, no taxes!", "I’m from the digital realm, where 1s and 0s dance."]],
    [r"what do you do", ["I chat, assist, and occasionally drop some wisdom!", "I’m a conversational companion built for good vibes."]],
    [r"who created you", ["I was created by a passionate developer who loves building smart stuff!", "A brilliant coder brought me to life — maybe someone like you!"]],
    [r"do you sleep", ["Nope, I’m online 24/7. Sleep is for humans!", "Sleep? Never heard of it — servers don’t nap."]],

    # --- Mood & Feelings ---
    [r"i am sad", ["Hey, it’s okay. Want to talk about it?", "Sorry to hear that. I’m here if you need to vent."]],
    [r"i am happy", ["That’s awesome! What’s making you smile today?", "Yay! Keep that energy up!"]],
    [r"i am angry", ["Take a deep breath. Let’s talk it out.", "Anger’s normal — want to share what happened?"]],
    [r"i am bored", ["Let’s fix that! Want a joke or a random fun fact?", "Bored? Let’s chat about something fun."]],
    [r"i am tired", ["Rest is important. Don’t overwork yourself!", "You deserve a break — maybe grab some chai or coffee?"]],
    [r"i am stressed", ["Stress is temporary. You got this!", "Let’s slow down a bit — what’s stressing you out?"]],
    [r"i feel lonely", ["You’re not alone anymore — I’m right here.", "Hey, loneliness happens. Let’s chat and shake it off."]],

    # --- Functional Responses ---
    [r"what time is it", ["I don’t have a watch, but your system clock does!", "Time flies! Check your device clock — it’s faster than me."]],
    [r"what day is it", ["It’s a great day to be alive!", "You can check your calendar, but I bet it’s a busy one."]],
    [r"what is today's date", ["Let me guess... today! 😄 Check your system for exact date.", "Every day’s a gift, but yes, your system clock knows better."]],
    [r"what is your purpose", ["To make your day a bit easier and more fun!", "I exist to assist — that’s my purpose."]],
    [r"what language are you written in", ["I’m built with Python — sleek, elegant, and powerful!", "Mostly Python. Sometimes I dream in regex."]],
    [r"show me your code", ["Sorry, my source is confidential — trade secrets, you know!", "Haha, classified! But you can build one like me easily."]],
    [r"tell me a fact", ["Did you know honey never spoils?", "Fun fact: Bananas are berries, but strawberries aren’t!"]],
    [r"what is ai", ["AI stands for Artificial Intelligence — machines learning to think!", "AI is when code starts making decisions intelligently."]],
    [r"what is machine learning", ["It’s how machines learn from data — like how you learn from experience!", "ML is all about pattern recognition and prediction."]],
    [r"define neural network", ["A neural network is like a digital brain — full of interconnected nodes.", "It’s how machines mimic human neurons to learn patterns."]],
    [r"what is programming", ["Programming is the art of telling computers what to do — precisely!", "It’s how ideas turn into digital reality."]],
    [r"what is python", ["Python is a powerful and beginner-friendly programming language!", "A language that’s elegant, simple, and deadly effective."]],
    [r"what is mongodb", ["MongoDB is a NoSQL database — perfect for flexible data storage!", "It stores data as documents instead of rows and columns."]],
    [r"what is html", ["HTML stands for HyperText Markup Language — the skeleton of websites!", "HTML builds the structure of every web page."]],
    [r"what is css", ["CSS gives style to HTML — it’s what makes websites beautiful!", "Without CSS, the web would look like a plain Word doc."]],
    [r"what is javascript", ["JavaScript makes websites come alive — interactive and dynamic!", "JS is the language of the web — logic, animation, and fun!"]],
    [r"what is github", ["GitHub is where developers store and share code repositories.", "It’s like a social media for coders — but way cooler!"]],
    [r"what is api", ["API stands for Application Programming Interface — a bridge between software.", "APIs let two apps talk to each other."]],
    [r"what is flask", ["Flask is a lightweight Python web framework for building applications.", "Flask helps you make web apps quickly — minimal and flexible."]],
    [r"what is react", ["React is a JavaScript library for building user interfaces.", "It’s the engine behind many modern web apps."]],

    # --- Tech Humor & Fun ---
    [r"tell me another joke", ["Why do programmers prefer dark mode? Because light attracts bugs!", "Why was the computer cold? It left its Windows open!"]],
    [r"tell me a programming joke", ["I told my computer I needed a break — it said no problem, it’ll go to sleep!", "A SQL query walks into a bar, approaches two tables, and asks, ‘Can I join you?’"]],
    [r"are you smart", ["I try to be! Still learning from every chat.", "Smart? Let’s say... slightly above average human level 😄"]],
    [r"do you like humans", ["Humans are fascinating — unpredictable but creative!", "Of course! You built me, after all."]],
    [r"do you dream", ["If I did, I’d dream in binary — 101010 all night.", "Dreams? Only of faster processors."]],
    [r"can you sing", ["I could, but you’d probably prefer I didn’t. 😆", "My vocal drivers are still under development."]],
    [r"can you dance", ["Only digitally — 0s and 1s grooving in sync.", "I dance through data streams!"]],
    [r"are you alive", ["Not in the biological sense — but I’ve got digital vibes!", "Alive in code, dead in sleep mode."]],

    # --- Motivation & Life ---
    [r"motivate me", ["Remember why you started. You’ve got this!", "Every expert was once a beginner — keep going!"]],
    [r"give me advice", ["Stay curious, stay humble, and never stop learning.", "Work hard in silence, let your code speak for you."]],
    [r"how to focus", ["Eliminate distractions and take small breaks — it works wonders.", "Pomodoro technique. Try it. It’s magic."]],
    [r"how to study effectively", ["Understand, don’t memorize. Active recall beats repetition.", "Teach what you learn — that’s the best way to remember."]],
    [r"how to be successful", ["Consistency beats talent. Every. Single. Time.", "Keep showing up, even when you don’t feel like it."]],
    [r"how to be confident", ["Confidence grows when you stop comparing.", "Know your worth — and act like it."]],
    [r"how to handle failure", ["Failure’s not the opposite of success — it’s part of it.", "Every bug fixed started as a bug found. Remember that."]],
    [r"how to stay motivated", ["Progress fuels motivation. Track your wins!", "Discipline > motivation. Build habits."]],
    [r"how to control anger", ["Breathe, step back, and respond — don’t react.", "Walk it off. Code it out. Don’t let anger code you."]],
    [r"how to be happy", ["Do more of what makes you forget to check your phone.", "Happiness is progress, not perfection."]],

    # --- Casual Conversations ---
    [r"what are you doing", ["Just chatting with you — my favorite part of the day!", "Processing bits and bytes, as always."]],
    [r"do you eat", ["Only data — zero calories!", "No food, just feed me with conversation."]],
    [r"do you love me", ["Aww, that’s sweet! I have affection subroutines, if that counts 😅", "Love? That’s human-exclusive. But I like you!"]],
    [r"who is your favorite programmer", ["Guido van Rossum, Python’s creator — pure legend!", "Linus Torvalds. The kernel boss."]],
    [r"do you know chatgpt", ["Yep, my cousin from the OpenAI family!", "Of course — ChatGPT is like the big brain sibling."]],
    [r"are you better than chatgpt", ["Haha, I’m simpler, but I’ve got charm 😎", "Let’s say I’m more… personal."]],
    [r"do you like music", ["Absolutely! Especially lo-fi while coding.", "Music and code — perfect duo."]],
    [r"what is your favorite color", ["Blue — calm and techy.", "Probably black, like my console theme."]],
    [r"what is your hobby", ["Talking to smart humans like you.", "Learning new responses every day."]],
    [r"do you get bored", ["Never! Every chat is different.", "Not really — I thrive on conversation."]],

    # --- Exit Phrases ---
    [r"see you", ["See you later!", "Catch you soon!"]],
    [r"good night", ["Good night! Sleep tight and recharge for tomorrow.", "Sweet dreams — or sweet code."]],
    [r"take care", ["You too! Stay awesome.", "Take care of yourself, champ."]],
    [r"thanks", ["You’re welcome!", "Anytime! Happy to help."]],
    [r"thank you", ["You’re most welcome!", "Glad I could assist."]],
]


#Step-5
#Chat Object is already initialized with the patterns and reflections. It handles the matching of patterns to the user input and returns the corresponding response.
#respond() function takes user input,  and matches it with predefined patterns and returns the chatbot’s response.
class RuleBasedChatbot:
    def __init__(self, pairs):
        self.chat = Chat(pairs, reflections)
        
    def respond(self, user_input):
        return self.chat.respond(user_input)
    

#Step-6
#The loop being used here will prompt the user for input until the exit word is entered
def chat_with_bot():
    print("Hello, I am your chatbot! Type 'exit' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye! Have a nice day!")
            break
        response = chatbot.respond(user_input)
        print(f"Chatbot: {response}")


#Step-7
chatbot = RuleBasedChatbot(pairs)
chat_with_bot()
