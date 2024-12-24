import random

# Define mappings and outcomes
youDict = {"s": 1, "w": -1, "g": 0}
reverseDict = {1: "snake", -1: "water", 0: "gun"}
outcomeDict = {
    (1, -1): "you win",
    (1, 0): "you lose",
    (-1, 1): "you lose",
    (-1, 0): "you win",
    (0, -1): "you win",
    (0, 1): "you lose"
}

# Get computer and player choices
computer = random.randint(-1, 1)
youStr = input("Enter your choice (s for snake, w for water, g for gun): ").lower()
you = youDict[youStr]

# Print choices
print(f"You choose: {reverseDict[you]}\nComputer choose: {reverseDict[computer]}")

# Determine the outcome
if computer == you:
    print("tie")
else:
    print(outcomeDict[(you, computer)])
