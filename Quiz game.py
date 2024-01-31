import random

class QuizGame:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def display_welcome_message(self):
        print("\nWelcome to the Quiz Game!")
        print("Answer the following questions to test your knowledge.")
        print("Let's get started!\n")

    def present_quiz_questions(self):
        print("Please type the option code corresponding to the correct answer\n")
        random.shuffle(self.questions)
        for index, question in enumerate(self.questions, start=1):
            print(f"Question {index}: {question['question']}")
            for option in question['options']:
                print(f"   {option}")
            user_answer = input("Your answer: ").strip().lower()
            self.evaluate_user_answer(user_answer, question['correct_answer'])

    def evaluate_user_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer.lower():  
            print("Correct!\n")
            self.score += 1
        else:
            print(f"Incorrect!\nThe correct answer is: {correct_answer}\n")

    def display_final_results(self):
        print("Quiz completed!")
        print(f"Your final score is: {self.score}/{len(self.questions)}")
        print("Thanks for playing!")

    def play_again(self):
        return input("Do you want to play again? (yes/no): ").strip().lower() == "yes"

quiz_questions = [
    {
        'question': 'Who is the founder of the company SpaceX?',
        'options': ['A. Elon Musk', 'B. Steve Jobs', 'C. Mark Zuckerberg', 'D. Richard Branson'],
        'correct_answer': 'A'
    },
    {
        'question': 'What is the full form of RAM?',
        'options': ['A. Remote Access Memory', 'B. Read Access Memory', 'C. Random Access Memory', 'D. Random Active Memory'],
        'correct_answer': 'C'
    },
    {
        'question': 'How many oxygen atoms are there in an atom of oxygen gas?',
        'options': ['A. 1', 'B. 2', 'C. 3', 'D. 4'],
        'correct_answer': 'B'
    },
    {
        'question': 'Who painted the Mona Lisa?',
        'options': ['A. Leonardo da Vinci', 'B. Pablo Picasso', 'C. Vincent van Gogh', 'D. Claude Monet'],
        'correct_answer': 'A'
    },
    {
        'question': 'What is the currency of Germany?',
        'options': ['A. Yen', 'B. Dollar', 'C. Pound', 'D. Euro'],
        'correct_answer': 'D'
    },
]

def main():
    while True:
        game = QuizGame(quiz_questions)
        game.display_welcome_message()
        game.present_quiz_questions()
        game.display_final_results()
        
        if not game.play_again():
            print("Thanks for playing. Goodbye!")
            break

if __name__ == "__main__":
    main()