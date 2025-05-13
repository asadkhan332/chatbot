def greet_user(name):
    return f"Hello {name} , i'm Chatbot , Your university assitant"

def help_menu():
    return(
        "You can ask me:\n" 
        "1.what is your name:\n"
        "2. what can you do:\n" 
        "3. what is computer science:\n"
        "4. list some CS subjects:\n"
        "5. recommend some programming languages:\n"
        "6. how to improve coding:\n" 
        "7. exit:\n"
    )
def subject_list():
    subjects = [
        "Data Structures",
        "Algorithms",
        "Operating Systems",
        "Computer Networks",
        "Database Systems",
        "Artificial Intelligence",
        "Machine Learning"
    ]
    return "Here are Some CS Subjects:\n-" + "\n-".join(subjects)
def process_input(user_input):
    """Process user queries with conditional Logic."""
    user_input = user_input.lower()
    if user_input in ["what's your name" , "what is your name"]:
        return "my name is Minibot i am here to asisst CS students!"
    elif user_input == "what can you do":
        return "I can guide you with CS info, subject help, coding tips and more"
    elif user_input == "what is computer science":
        return (
                   "Computer Science is the study of computers, algorithms, and how to solve problems using technology 🖥️"
        )
    elif user_input == "list some cs subjects":
        return subject_list()
    elif user_input == "recommend programming languages":
        return(
            "Here are some top programming languages to learn:\n"
            "- Python 🐍 (Easy & powerful)\n"
            "- Java ☕ (OOP and widely used)\n"
            "- JavaScript 🌐 (For Web Dev)\n"
            "- C++ 🚀 (For performance)\n"
            "- Rust 🦀 (For safety and speed)"
        )
    elif user_input == "how to improve coding":
        return(
            "Practice daily on platforms like LeetCode, HackerRank.\n"
            "Build small projects. Read others' code. Stay curious! "
        )
    elif user_input == "exit":
        return ("Thanks for Chatting Goodbye!....😃")
    else:
        return "Sorry i did'nt get that . 'Type' help to see other option"
def run_minibot():
    """"Main Chat bot Runner."""
    print("Welcome to MiniBot , You CS assistant ")
    name = input(" Please! Enter your name : ")
    print(greet_user(name))

    while True:
        print("\nType 'help' to see options or 'exit' to quit. ")
        user_input = input("You: ")
        if user_input.lower() == "help":
            print(help_menu())
        else:
            response = process_input(user_input)
            print("Mini Bot: ", response)
            
        if user_input.lower() == "exit":
            break
# Run the Chatbot
run_minibot()
