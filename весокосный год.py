try :
    a=int(input("введите a"))
except :
    print("you'll be banned in 5 seconds")
if a % 4==0:
    if a % 100==0:
        if a % 400 == 0:
            print("Високосный")
        else:
            print("Невисокосный")
    else :
        print("Високосный")

else :
    print("Невисокосный")
