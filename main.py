from random import choice
from art import logo
from art import vs
from game_data import data
# from replit import clear


def print_subject_info(selected_subject, letter):
    print(f"Compare {letter}: {selected_subject['name']}, a {selected_subject['description']},"
          f" from {selected_subject['country']}.")
    # print("DEBUG: " + str(selected_subject['follower_count']) + " follower_count.")


game = "in-progress"


while game == "in-progress":
    # clear()

    score = 0
    subject_a = choice(data)
    round = "in-progress"


    while round == "in-progress":
        # clear()

        subject_b = choice(data)

        print(logo)

        print_subject_info(subject_a, "A")

        print(vs)

        while subject_a == subject_b:
            # print("DEBUG: (RE-ROLLING) - IDENTICAL SUBJECTS.")
            subject_b = choice(data)

        print_subject_info(subject_b, "B")

        guess = input(f"SCORE: {score} | Who has more followers? Type 'A' or 'B': ").lower()

        if guess == "a":
            if subject_a['follower_count'] > subject_b['follower_count']:
                print("CORRECT!")
                score += 1
            else:
                print("WRONG!")
                round = "stop."
                score = 0
        elif guess == "b":
            if subject_b['follower_count'] > subject_a['follower_count']:
                print("CORRECT!")
                subject_a = subject_b
                score += 1
            else:
                print("WRONG!")
                round = "stop."
                score = 0
        else:
            round = "ERROR."
