questions = [
    {
        "question": "Which command shows the current directory?",
        "options": ["A. ls", "B. pwd", "C. cd"],
        "answer": "B"
    },
    {
        "question": "Which command lists files and folders?",
        "options": ["A. ls", "B. mkdir", "C. rm"],
        "answer": "A"
    },
    {
        "question": "Which command creates a new directory?",
        "options": ["A. cd", "B. pwd", "C. mkdir"],
        "answer": "C"
    },
    {
        "question": "Which command changes the current directory?",
        "options": ["A. cd", "B. ls", "C. cp"],
        "answer": "A"
    },
    {
        "question": "Which command copies a file?",
        "options": ["A. mv", "B. cp", "C. rm"],
        "answer": "B"
    }
]

score = 0

print("Welcome to the Linux Command Quiz!")
print("----------------------------------")

for question in questions:
    print("\n" + question["question"])

    for option in question["options"]:
        print(option)

    answer = input("Your answer (A, B or C): ").upper()

    if answer == question["answer"]:
        print("Correct!")
        score += 1
    else:
        print("Wrong answer!")
        print("Correct answer:", question["answer"])

print("\nQuiz finished!")
print("Your score:", score, "/", len(questions))
