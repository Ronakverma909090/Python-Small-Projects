print("Welcome to the game")
print("Do you want to play? Type yes or no.")
playing = input()

if playing != "yes":
    quit()

score = 0

answer = input("What does the RAM stands for?")
if answer.lower() == "random access memory":
    print("Correct!")
    score += 1
else:
    print("incorrect")

answer2 = input('What does CPU stands for?')
if answer2.lower() == 'central processing unit':
    print('correct!')
    score += 1
else:
    print("incorrect")

answer3  = input('What does ROM stands for?').lower()
if answer3 == 'read only memory':
    print('Correct!')
    score += 1
else:
    print("incorrect")

answer4 = input('What color is a banana?').lower()
if answer4 == 'yellow':
    print('correct!')
    score += 1
else:
    print("incorrect")

answer5 = input('What color is a orange?').lower()
if answer5 == 'orange':
    print('Correct!')
    score += 1
else:
    print("incorrect")



print(f"The game is finished, your total score is {score} out of 5")