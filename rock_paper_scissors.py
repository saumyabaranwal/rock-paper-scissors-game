from random import randint

print("=" * 50)
print("🎉 Welcome to Rock, Paper, Scissors — Childhood Rewind Edition 🎉")
print("=" * 50)
print('''
📜 The Rules:
1️⃣ Rock beats Scissors
2️⃣ Scissors beats Paper
3️⃣ Paper beats Rock

🔤 Make sure to type correctly! (case-insensitive)
🎯 Let's see if you can beat the computer!
''')

choices = ["rock", "paper", "scissors"]
player_score = 0
comp_score = 0

try:
    n = int(input("💡 How many rounds do you want to play? "))
except ValueError:
    print("❌ That's not a valid number. Exiting game.")
    exit()

print("\n🕹️ Game Start!\n" + "-" * 30)

for i in range(1, n + 1):
    print(f"\n🎲 Round {i}")
    comp = choices[randint(0, 2)]
    player = input("👉 Your choice (rock/paper/scissors): ").strip().lower()

    if player not in choices:
        print("⚠️ Invalid input! Please check your spelling.")
        continue

    print(f"🤖 Computer chose: {comp}")

    if player == comp:
        print("🔁 It's a tie!")
    elif (player == "rock" and comp == "scissors") or \
         (player == "scissors" and comp == "paper") or \
         (player == "paper" and comp == "rock"):
        print(f"✅ You win! {player.capitalize()} beats {comp}")
        player_score += 1
    else:
        print(f"❌ You lose! {comp.capitalize()} beats {player}")
        comp_score += 1

print("\n🎮 Game Over!\n" + "=" * 30)
print(f"🏁 Final Score: You {player_score} - Computer {comp_score}")

if player_score > comp_score:
    print("🏆 You're the ultimate winner! GG!")
elif player_score < comp_score:
    print("💻 Computer wins this time. Better luck next time!")
else:
    print("🤝 It's a tie overall! Well played.")

print("✨ Thanks for playing! Come back soon! ✨")
