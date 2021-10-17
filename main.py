# OOP enables modularity at its best!; Object-Oriented Programming > Procedural Programming

from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# question_bank = [
#     Question(text=q_and_a['text'], answer=q_and_a['answer']) for q_and_a in question_data
# ]
question_bank = [
    Question(q_and_a['question'], q_and_a['correct_answer']) for q_and_a in question_data
]

# print(question_bank)

quiz = QuizBrain(question_bank)
# quiz.next_question()

while quiz.still_has_questions():
    quiz.next_question()

print('You\'ve completed the quiz.')
print(f'Your final score is: {quiz.user_score}/{quiz.current_question_number}')

# NOTE: JSON stands for JavaScript Object Notation

# see how after all the changes that we made to the actual quiz data (i.e. the list of dictionaries with its respective
# key:value pairs - only the main.py file cares about the changes of/to the implementation of the various modules used
# in our quiz (game/project) - that is BIG ADVANTAGE of OOP

# JUST KEEP GOING!
