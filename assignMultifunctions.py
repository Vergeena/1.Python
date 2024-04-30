class moFunctions():
    def subfields():
        name=input("Subfilelds in AI are:")
        print("Machine Learning")
        print("Neural Networks")
        print("Vision")
        print("Robotics")
        print("Speech Processing")
        print("Natural Language Processing")
    subfields()

    def oddeven():
        num=int(input("Enter a number:"))
        if((num%2)==0):
            print(num,"is even number")
        else:
            print(num,"is odd number")
    oddeven()       

    def EliorNot():
        gen=input("Your gender:")
        age=int(input("Your age:"))
        if(gen=="Male"):
            if(age<21):
                print("NOT ELIGIBLE")
            else:
                print("ELIGIBLE")
        elif(gen=="Female"):
            if(age<21):
                print("NOT ELIGIBLE")
            else:
                print("ELIGIBLE")
    EliorNot()

    def percentage():
        subject1=98
        print("subject1=98")
        subject2=87
        print("subject2=87")
        subject3=95
        print("subject3=95")
        subject4=95
        print("subject3=95")
        subject5=93
        print("subject3=93")
        Marks=subject1+subject2+subject3+subject4+subject5
        print("Total:",Marks)
        per=float(Marks)*(100/500)
        print("Percentage is: ",per)
    percentage()

    def size():
        Height=int(input("Height:"))
        Breadth=int(input("Breadth:"))
        Area=(Height*Breadth)/2
        print("Area of Triangle:",Area)
        Height1=int(input("Height1:"))
        Height2=int(input("Height2:"))
        Breadth=int(input("Breadth:"))
        peri=(Height1+Height2+Breadth)
        print("Perimeter of Triangle:",peri)
    size()

