from pathlib import Path

# Get questions and answers from file

data_folder = Path("resource/")
user_folder = data_folder / "user"
qFile = data_folder / "question.txt"
aFile = data_folder / "answer.txt"

# Check if the files exist
if qFile.exists():
    questions = qFile.read_text().splitlines()
else:
    print("There is no quiz file")

if aFile.exists():
    with open(aFile, "r") as read_file:
        answers = read_file.read().splitlines()
else:
    print("There is no correct answer file")

# create variable to collect user info, answers and total score
username = input("What is your name?\n")
userAnswer = []
score = 0
print("\n")

# Use For-loop to ask questions and get answers from
for i in range(len(questions)):
    userAnswer.append(input(str(i + 1) + ") " + questions[i] + "\n" + "Answer: "))
    if userAnswer[i].casefold() == answers[i].casefold():
        print("Correct!\n")
        score += 1
    else:
        print("Wrong!\n")

# Create a new file to store user's answers
new_file = user_folder / str(username + ".txt")
sub_name = 1

# Check if there is any file with the same name, re-name if file exists
while new_file.exists():
    new_file = user_folder / str(username + str(sub_name) + ".txt")
    sub_name += 1

# Write all answers to the file
with open(new_file, "w") as write_file:
    for i in range(len(userAnswer)):
        write_file.write(userAnswer[i])
        if i < len(userAnswer) - 1:
            write_file.write("\n")

# Final report
print("\tyour answers are saved.")
print("\tYour total score is", str(score) + "/10")