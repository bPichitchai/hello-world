# Create a list of questions and answers
quizzes = [
    "1.) what is the capital of Australia?\n",
    "2.) what is the capital of Australia?\n",
    "3.) what is the capital of Australia?\n",
    "4.) what is the capital of Australia?\n",
    "5.) what is the capital of Australia?\n",
    "6.) what is the capital of Australia?\n",
    "7.) what is the capital of Australia?\n",
    "8.) what is the capital of Australia?\n",
    "9.) what is the capital of Australia?\n",
    "10.) what is the capital of Australia?\n",
]
answers = [
    "CANBERRA",
    "CANBERRA",
    "CANBERRA",
    "CANBERRA",
    "CANBERRA",
    "CANBERRA",
    "CANBERRA",
    "CANBERRA",
    "CANBERRA",
    "CANBERRA",
]

# create variable to collect a total score
score = 0

# Use For-loop to ask questions and get answers from user

for i in range(len(quizzes)):
    if input(quizzes[i]).casefold() == answers[i].casefold():
        print("Correct!")
        score += 1
    else:
        print("Wrong!")

print("\n\t", "Your total score is", str(score) + "/10")
