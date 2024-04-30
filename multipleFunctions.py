class Multifunction():
    def num():
        num=int(input("Enter the BMI index:"))
        if(num<18.5):
            print("Under weight")
            message="Under weight"
        elif(num<24.9):
            print("Normal Range")
            message="Normal Range"
        elif(num<29.9):
            print("Overweight")
            message="Overweight"
        else:
            print("Very Overweight")
            message="Very Overweight"
        return message

    def oddeven():
        num=int(input("Enter the number whether it even or odd:"))
        if((num%2)==1):
            print("The number is odd number")
            message="odd number"
        else:
            print("The number is even number")
            message="even number"
        return message