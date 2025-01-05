import os

# File names for questions and scores
QUESTIONS_FILE = 'questions.txt'
SCORES_FILE = 'scores.txt'

# Function to load questions from a file
def load_questions():
    questions = []
    try:
        with open(QUESTIONS_FILE, 'r') as file:
            for line in file:
                parts = line.strip().split(',')
                if len(parts) == 6:
                    question = {
                        'question': parts[0],
                        'options': parts[1:5],
                        'answer': parts[5].strip().upper()
                    }
                    questions.append(question)
    except FileNotFoundError:
        print(f"Error: {QUESTIONS_FILE} not found.")
    return questions

# Function to save score to a file
def save_score(user_name, score, total):
    with open(SCORES_FILE, 'a') as file:
        file.write(f"{user_name},{score}/{total}\n")

# Main function to run the quiz
def run_quiz():
    questions = load_questions()
    if not questions:
        print("No questions available. Please check the questions file.")
        return

    print("Welcome to the Quiz Application!")
    print("Rules:\n- Each question has 4 options.\n- Enter the option (A, B, C, D) as your answer.")
    input("Press Enter to start the quiz!")

    score = 0
    total_questions = len(questions)

    for i, question in enumerate(questions):
        print(f"\nQuestion {i + 1}: {question['question']}")
        for j, option in enumerate(['A', 'B', 'C', 'D']):
            print(f"{option}. {question['options'][j]}")
        user_answer = input("Your Answer: ").strip().upper()

        if user_answer == question['answer']:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer was {question['answer']}.")

    print(f"\nQuiz Complete!\nYour Score: {score}/{total_questions}")

    user_name = input("Enter your name to save your score: ").strip()
    if user_name:
        save_score(user_name, score, total_questions)
        print(f"Score recorded in {SCORES_FILE}.")
    else:
        print("Score not saved.")

if __name__ == "__main__":
    run_quiz()
