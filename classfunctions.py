class subfieldsInAI():
    def subfields():
        print("Sub-fields in AI are:")
        List = ('Machine Learning', 'Neural Networks', 'Vision', 'Robotics', 'Speech Processing', 'Natural Language Processing')
        for s in List:
            print(s)

    def oddEven():
        num = int(input("Enter a number:"))
        if (num % 1)==1:
            print(num, "is a Odd number")
        else:
            print(num, "is a Even number")

    def eligible():
         gender = input("Your Gender:")
         age = int(input("Your Age:"))
         if (age<21):
             print("Not Eligible")
         else:
             print("Eligible")   

    def percentage():
        sub1 = int(input("Subject1="))
        sub2 = int(input("Subject2="))
        sub3 = int(input("Subject3="))
        sub4 = int(input("Subject4="))
        sub5 = int(input("Subject5="))
        Total = sub1+sub2+sub3+sub4+sub5
        print("Total:", sub1+sub2+sub3+sub4+sub5)
        per = (Total / 500) * 100
        print("percentage:", per)

    def triangle():
        a = int(input("Height:"))
        b = int(input("Breadth:"))
        print("Area Formula:, (Height*Breadth)/ 2")
        print("Area of Triangle:", (a*b)/ 2)
        a1 = int(input("Height1:"))
        a2 = int(input("Height2:"))
        b2 = int(input("Breadth2:"))
        print("Perimeter Formula:, Height1+Height2+Breadth2")
        print("Perimeter of Triangle:", a1+a2+b2)