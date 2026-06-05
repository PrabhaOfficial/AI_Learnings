class multiFunction():
    def bmi (weight,height):
        bmi = weight/(height ** 2)
        print("The BMI index is",bmi)
        if (bmi < 18.5):
            return "underweight"
        elif (18.5 <= bmi <= 24.9):
            return "normal"
        elif (25 <= bmi <= 29.9):
            return "overweight"
        elif (bmi > 30):
            return "very weight"

    def findAgeCategoryNoReturn (age):    
        if(age<18):
            print("Children")
        elif(age<35):
            print("Adult")
        elif(age<59):
            print("Citizen")
        else:
            print("Senior Citizen")

    def findAgeCategory (age):    
        if(age<18):
            return "Children"
        elif(age<35):
            return "Adult"
        elif(age<59):
            return "Citizen"
        else:
            return "Senior Citizen"

    def triangle():
        height = int(input("Height:"))
        breadth = int(input("Breadth:"))
        print("Area  formula: (Height*Breadth)/2")
        area= (float)(height*breadth)/2
        print("Area of triangle: ",area)
        height1 = int(input("Height1:"))
        height2 = int(input("Height2:"))
        breadth = int(input("Breadth:"))
        print("Perimeter formula: Height1+Height2+Breadth")
        peri= height1+height2+breadth
        print("Perimeter of triangle: ",peri)

    def percentage():
        sub1 = int(input("Subject1= "))
        sub2 = int(input("Subject2= "))
        sub3 = int(input("Subject3= "))
        sub4 = int(input("Subject4= "))
        sub5 = int(input("Subject5= "))
        total = sub1+sub2+sub3+sub4+sub5
        per=total/5
        print ("Total: " , total)
        print("Percentage: ", per)

    def Eligible(age,gender):
        if(gender == "male"):        
            if (age < 21):
                return ("Not Eligible")
            else:
                return ("Eligible")
        elif(gender == "female"):
            if (age < 18):
                return ("Not Eligible")
            else:
                return ("Eligible")

    def oddEven(num):
        if (num%2 == 0):
            print(num,"is a Even number")
        else:
            print(num,"is a Odd number")

    def Subfields(subFds):
        print("Sub-fields in AI are:")
        for field in subFds:
            print(field)

        