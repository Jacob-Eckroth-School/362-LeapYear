


def main():
   
   
    number = input("Please enter the year you want to check for leapyear status:")
    intNumber = int(number)

    if(intNumber % 400 == 0):
        print("The year " + number + " is a leap year!")
    elif(intNumber %  100 == 0):
        print("The year " + number + " is not a leap year.")
    elif(intNumber % 4 == 0):
        print("The year " + number  +" is a leap year!")
    else:
        print("The year " + number + " is not a leap year." )



if __name__ == "__main__":
    main()