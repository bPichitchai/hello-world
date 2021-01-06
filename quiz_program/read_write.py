from pathlib import Path

# Get file path for questions
data_folder = Path("resource/")
file_name = "question.txt"
data_file = data_folder / file_name

# Read text file using 'pathlib'
questions = data_file.read_text().splitlines()

# Open and read file using 'open' function and 'with' statement
with open(data_file, "r") as qFile:
    if qFile.readable():
        # questions = qFile.readlines()
        questions = qFile.read().splitlines()

for i in questions:
    print(i)
