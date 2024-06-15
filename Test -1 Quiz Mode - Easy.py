print ("Welcome to the world of JRRY!")

playing = input("Do you want to play? ")

if playing.lower()  != "yes":
    quit()
    
print ("Okay let's playy :)")

score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit": 
    print ('Correct!!')
    score += 1
else: 
    print ("Incorrect :(")
    
answer = input("How to move the pointer icon on desktop? ")
if answer.lower() == "mouse": 
    print ('Correct!!')
    score += 1
else: 
    print ("Incorrect :(")

answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit": 
    print ('Correct!!')
    score += 1
else: 
    print ("Incorrect :(")

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory": 
    print ('Correct!!')
    score += 1
else: 
    print ("Incorrect :(")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score/4) * 100) + "%.")