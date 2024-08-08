import random
from ask_questions import ask_question, calculate_result 
from quiz import get_questions, shuffle_questions

def main():
    """Main function to run the quiz application."""
    questions = get_questions()  # Step 1: Get questions
    shuffled_questions = shuffle_questions(questions)  # Step 2: Shuffle questions
    
    score = 0  # Initialize score
    total_questions = len(shuffled_questions)
    
    # Step 3: Ask each question
    for question in shuffled_questions:
        if ask_question(question):
            score += 1
    
    # Step 4: Calculate result and display final score
    result = calculate_result(score, total_questions)
    print(f"Quiz completed! Your final score is {score} out of {total_questions}.")
    print(f"Result: {result}")
    
    if result == "Pass":
        print("Congratulations, you passed the quiz!")
    else:
        print("Unfortunately, you did not pass the quiz. Better luck next time!")

if __name__ == "__main__":
    main()