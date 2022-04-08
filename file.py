
# computer Quiz
print("Welcome to my computer quiz!")
playing = input("Do you want to play? ")
# print(playing)

if playing != "yes":
    quit()

print("Okay! Let's play :)")

answer = input("What does CPU stand for? ")
if answer == "central processing unit":
    print('Correct!')
else:
    print("Incorrect!")

playing = input("Do you want to play again? ")  
if playing != "yes":
        quit()

print("Okay! Let's play again :)")

answer = input("What does Iot stand for? ")
if answer == "Internet of things":
    print('Correct!')
else:
    print("Incorrect!")