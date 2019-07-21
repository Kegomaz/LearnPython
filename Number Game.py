import random
secret = random.randint(1,10)
print("-----Guess Which Number I'm Thinking Right Now-------")
temp = input("guess which number i'm thinking right now")
guess = int(temp)
while guess != secret:
    temp = input("sorry, it isnt correct, please try again so the numer is:")
    guess = int(temp)
    if guess == secret:
        print("what, you really got me!")
        print("but it's only a start")
    else:
        if guess > secret:
            print("sorry, it's a bit big")
        else:
            print("nope, it's too small for me")
print("In End")
