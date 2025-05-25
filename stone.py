import random

choices = ["rock", "paper", "scissors"]
art = {"rock": "🪨", "paper": "📄", "scissors": "✂️"}
player_score = 0
computer_score = 0

while True:
    player_choice = input("\nChoose rock, paper, or scissors: ").lower()
    while player_choice not in choices:
        print("Invalid choice! Try again.")
        player_choice = input("Choose rock, paper, or scissors: ").lower()

    computer_choice = random.choice(choices)
    print(f"\nYou chose: {art[player_choice]}  Computer chose: {art[computer_choice]}")

    if player_choice == computer_choice:
        print("It's a tie!")
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "paper" and computer_choice == "rock") or \
         (player_choice == "scissors" and computer_choice == "paper"):
        print("You win!")
        player_score += 1
    else:
        print("Computer wins!")
        computer_score += 1

    print(f"Score - You: {player_score} | Computer: {computer_score}")

    play_again = input("\nPlay again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thanks for playing!")
        break
