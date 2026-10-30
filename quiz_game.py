print("===== WELCOME TO PYTHON QUIZ =====")

score = 0

answer = input("1. Which language are we learning? ")

if answer.lower() == "python":
    print("Correct answer!")
    score += 1
else:
    print("Wrong answer!")

answer = input("2. What is 5 + 5? ")

if answer == "10":
    print("Correct answer!")
    score += 1
else:
    print("Wrong answer!")

answer = input("3. What is the capital of India? ")

if answer.lower() == "delhi":
    print("Correct answer!")
    score += 1
else:
    print("Wrong answer!")

print("\n===== QUIZ RESULT =====")
print("Your Score:", score, "/ 3")

if score == 3:
    print("Excellent! 🎉")
elif score >= 1:
    print("Good job! 👍")
else:
    print("Keep practicing! 💪")