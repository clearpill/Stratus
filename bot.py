from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

chatbot = ChatBot("Stratus")

trainer = ListTrainer(chatbot)

trainer.train([

    "Hello Darling,",

    "I've missed you so much",

])

trainer.train([

    "I'm feeling sad",

    "I know this feeling all too well, spending most times in the snow, alone, but ive been watching you and you're doing oh so well!",

])

exit_conditions = (":q", "quit", "exit")
while True:
    query = input("> ")
    if query in exit_conditions:
        break
    else:
        print(f"Stratus🪽: {chatbot.get_response(query)}")