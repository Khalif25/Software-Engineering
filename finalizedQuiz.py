import random # import random module

class Question:
    def __init__(self, SN, question, options, correct_answer):
        # initialize instances of objects
        self.serial_number = SN # give question with serial numbers
        self.question = question
        self.options = options
        self.correct_answer = correct_answer

    # show questions and options for each question lettered with ABC
    def display(self):
        print(f"{self.SN}. {self.question}")
        for i, option in enumerate(self.options, start=0):
            print(f"{chr(65+i)}. {option}") # label options with letters from A to C

    # This instance checks if answer provided by the user matches the correct answer
    def check_answer(self, selected_answer):
        return selected_answer.upper() == self.correct_answer.upper()

class Quiz:
    def __init__(self, questions, num_questions):
        self.questions = random.sample(questions, num_questions) # random selection of part of questions
        # with the user specifies the number of questions to answer at the outset

    def run(self, username):
        score = 0
        print(f"\nWelcome to the quiz, {username}!\n")
        for question in self.questions:
            question.display()
            try:
                user_choice = input("Enter the letter of your choice: ").upper() # ensure upper case letters are entered to ensure comparison of responses
                if user_choice not in ['A', 'B', 'C']:
                    raise ValueError("Invalid choice. Please enter A, B, or C.") # raise value error if other characters are select than those mentioned
                if question.check_answer(user_choice):
                    score += 1 # increment the score to 1 if the selected option matches the correct response
                    print("Correct!\n")
                else:
                    print(f"Incorrect. The correct answer is: {question.correct_answer}\n")
            except ValueError as e:
                print(e)
                continue

        print(f"\n{username}, you scored {score}/{len(self.questions)} ({(score/len(self.questions))*100:.2f}%)\n") # give the score for the user
        return score

def main():
    while True:
        scores = {} # dictionary for keeping a running score of the users
        users = [] # tuple for storing users
        while True:
            username = input("Enter your name (or 'quit' to end): ") # when name is entered the user is prompted to either ask if someone else wishes to take the quiz or quit the app
            if username.lower() == 'quit':
                break
            users.append(username) # add new usernames to the users tuple

        if users:
            # Quiz questions
            quiz_questions = [
                Question(1, "When did World War II end?", ["1945", "1951", "1939"], "C"),
                Question(2, "When was the UN established?", ["1945", "1946", "1950"], "A"),
                Question(3, "What is the capital of the US?", ["Washington", "Paris", "Vienna"], "A"),
                Question(4, "Which country has the highest proportion of citizens holding a doctoral degree?", ["China", "UK", "Luxembourg"], "A"),
                Question(5, "What does UN stand for?", ["United Nations", "Ultra Union", "Union NATO"], "A"),
                Question(6, "Which country recorded the most inventions since 1980?", ["United States", "UK", "Japan"], "A"),
                Question(7, "Which country has the most educated population in the world?", ["United States", "Finland", "Norway"], "B"),
                Question(8, "What is the greatest accomplishment of humanity country in the 21st century?", ["Space Explorations", "AI", "IoT"], "A"),
                Question(9, "Which country recorded the most inventions since 1980?", ["United States", "UK", "Japan"], "A"),
                Question(10, "Which country has the happiest population?", ["Norway", "Switzerland", "Finland"], "C")
            ]

            for user in users:
                while True:
                    try:
                        num_questions = int(input(f"{user}, enter the number of questions you want to answer: ")) # specify the number of question to answer (e.g. 5 questions)
                        if num_questions <= 0 or num_questions > len(quiz_questions):
                            raise ValueError(f"Please enter a number between 1 and {len(quiz_questions)}.") # enusre selected number is within questions number range (1-5)
                        break
                    except ValueError as e:
                        print(e)

                quiz = Quiz(quiz_questions, num_questions)
                score = quiz.run(user)
                scores[user] = score
        else:
            print("No users provided.")
            break
        # when quiz is finished then the user is prompted if anyone else wishes to take part the quiz
        if input("Is anyone else wishes to take the quiz? (yes/no): ").lower() != 'yes':
            break

    if scores: # if there are avaialable scores, find the user with the highest score
        highest_score = max(scores.values())
        highest_scoring_users = [user for user, score in scores.items() if score == highest_score]
        if highest_scoring_users:
            highest_scoring_users_string = ', '.join(highest_scoring_users)
            print(f"\nHighest Score: {highest_score} by {highest_scoring_users_string}")

        # summary of user scores
        average_score = sum(scores.values()) / len(scores) #  Calculate average scores of users
        print(f"Average Score: {average_score:.2f}") # print avg score

if __name__ == "__main__": # execute when the script is run directly
    main()
