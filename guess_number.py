import random
def guess():
    number =random.randint(0,100)
#    print("random number is %d" %(number))
    try:
        user = int(input("guess the number: "))
        result = cmp(user,number)
        if result == 0:
            print "you entered correct number"
        if result == -1:
            print "you entered too low"
        if result == 1:
            print "you entered too high"

    except NameError:
        print "please enter valid number"

guess()
