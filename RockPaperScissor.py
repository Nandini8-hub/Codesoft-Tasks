import random

def play_round():
    """Plays a single round of Rock, Paper, Scissors."""
    options = ["rock", "paper", "scissors"]
    user_choice = input("Choose rock, paper, or scissors: ").lower()

    while user_choice not in options:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        user_choice = input("Choose rock, paper, or scissors: ").lower()

    computer_choice = random.choice(options)

    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "win"
    else:
        return "lose"

def play_game():
    """Plays multiple rounds of Rock, Paper, Scissors."""
    user_score = 0
    computer_score = 0
    rounds = 0

    while True:
        rounds += 1
        result = play_round()

        if result == "win":
            user_score += 1
            print("You win this round!\n")
        elif result == "lose":
            computer_score += 1
            print("Computer wins this round!\n")
        else:
            print("It's a tie!\n")

        print(f"Current score: You - {user_score}, Computer - {computer_score}\n")

        play_again = input("Play another round? (yes/no): ").lower()
        if play_again != "yes":
            break

    print("Final Score:")
    print(f"You: {user_score}")
    print(f"Computer: {computer_score}")
    print("Thanks for playing!")

if __name__ == "__main__":
    play_game()