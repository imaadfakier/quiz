class QuizBrain:
    """
    ...
    """
    
    # ...
    
    def __init__(self, question_list, question_number=0, score=0):
        self.current_question_number = question_number
        self.question_list = question_list
        self.user_score = score

    # def next_question(self):
    #     if self.current_question_number <= len(self.question_list) - 1:
    #         self.current_question_number += 1
    #
    #         # user_option = input(self.question_list[self.current_question_number]['question'])  # wrong! Not this!
    #         user_option = input(f'Q.{self.current_question_number}: '
    #                                                                                 # we want this!
    #                             f'{self.question_list[self.current_question_number - 1].question} (True/False): ')

    def next_question(self):
        self.current_question_number += 1
        user_option = input(f'Q.{self.current_question_number}: '
                            f'{self.question_list[self.current_question_number - 1].question} (True/False): ')

        self.check_answer(user_option, self.question_list[self.current_question_number - 1].answer)

    def still_has_questions(self):
        return self.current_question_number <= len(self.question_list) - 1

    def check_answer(self, user_choice, correct_choice):
        if user_choice.lower() == correct_choice.lower():
            self.user_score += 1
            print('You got it right!')
        else:
            print('That\'s wrong!')

        print(f'The correct answer was: {correct_choice}')
        print(f'Your current score is: {self.user_score}/{self.current_question_number}.')
        print('\n')
