import datetime

print("===================================")
print("      WELCOME TO CHATBOT")
print("===================================")
print("Type 'bye' to exit the chatbot.\n")

while True:

    user = input("You: ").lower()

    if user == "hello" or user == "hi":
        print("Bot: Hello! Nice to meet you.")

    elif user == "how are you":
        print("Bot: I am doing great. Thanks for asking!")

    elif user == "what is your name":
        print("Bot: My name is Python ChatBot.")

    elif user == "time":
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print("Bot: Current time is", current_time)

    elif user == "date":
        current_date = datetime.datetime.now().strftime("%d-%m-%Y")
        print("Bot: Today's date is", current_date)

    elif user == "add":
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        print("Bot: Sum =", num1 + num2)

    elif user == "tell me a joke":
        print("Bot: Why did the computer go to the doctor?")
        print("Bot: Because it caught a virus!")

    elif user == "help":
        print("Bot: You can ask me:")
        print("- hello")
        print("- how are you")
        print("- what is your name")
        print("- time")
        print("- date")
        print("- add")
        print("- tell me a joke")

    elif user == "bye":
        print("Bot: Goodbye! Have a nice day.")
        break

    else:
        print("Bot: Sorry, I don't understand that.")