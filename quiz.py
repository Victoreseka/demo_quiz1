import random


def get_questions():
    """Define and return the list of quiz questions."""
    questions = [
        {
            "question": "What is the capital of France?",
            "choices": ["A) Paris", "B) London", "C) Rome", "D) Berlin"],
            "answer": "A"
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "choices": ["A) Earth", "B) Mars", "C) Jupiter", "D) Venus"],
            "answer": "B"
        },
        {
            "question": "Who wrote 'Romeo and Juliet'?",
            "choices": ["A) Charles Dickens", "B) George Orwell", "C) William Shakespeare", "D) Mark Twain"],
            "answer": "C"
        },
        {
            "question": "What is the largest ocean on Earth?",
            "choices": ["A) Atlantic Ocean", "B) Indian Ocean", "C) Arctic Ocean", "D) Pacific Ocean"],
            "answer": "D"
        },
        {
            "question": "What is the smallest prime number?",
            "choices": ["A) 0", "B) 1", "C) 2", "D) 3"],
            "answer": "C"
        },
        {
            "question": "What is the process by which plants convert sunlight, water, and carbon dioxide into glucose and oxygen?",
            "choices": ["A) Respiration", "B) Photosynthesis", "C) Decomposition", "D) Fermentation"],
            "answer": "B"
        }
    ]
    return questions

def shuffle_questions(questions):
    """Shuffle the order of questions to randomize the quiz."""
    random.shuffle(questions)
    return questions
