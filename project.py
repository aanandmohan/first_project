
print("WELCOME TO INFOBEAN LIBRARY ")
print("-------------***********------------------")
login=False
issue=False
finalName=""
finalday=0
while True:
    print("MENU ")
    print(" 1 login ")
    print(" 2 Book issue ")
    print(" 3 Return Book ")

    cohice=int(input("enter choice "))
    match cohice:
        case 1:
            name=input("Enter first name ")
            lastName=input("enter last name ")
            print(" 1 register as a  student ")
            print(" 2 register as a faculty ")
            choice2=int(input("enter choice "))
            finalName=name+lastName
            match choice2:
                case 1:
                    department=input("enter your department ")
                    branch=input("enter your branch ")
                    year=int(input("in which year your are right now "))
                    sem=int(input('enter your semseter '))
                    roll=int(input("enter your roll number "))
                    login=True
                    print()
                    print("THANK YOU FOR REGISTERTION ")
                case 2:
                    department=input("enter your department ")
                    facultyId=int(input("enter your faculty id "))
                    print()
                    print("THANKYU FOR REGISTRATION")
                    login=True
                case _:
                    print("Invalid choice please inter valid choice ")

        case 2:
            if login==False:
                print('please register yourself first ')
            else:
                print("-----WELCOME-----",finalName,"i hope you are doing well")
                print("Types of book ")
                print("1 academic ")
                print(" 2 fictional ")
                print(" 3 Non fictional ")
                choice3=int(input("enter what kind of book you want to issue "))
                print()
                match choice3:
                    case 1:
                        book=input("enter book name ")
                        days=int(input("enter for how many days you want to issue it "))
                        print("Book issue succesfully ")
                        finalday=days
                        issue=True
                    
                    case 2:
                        book=input("enter book name ")
                        author=input('enter author name ')
                        days=int(input("enter for how many days you want to issue it "))
                        finalday=days
                        issue=True

                        print("Book issue succesfully ")
                    case 3:
                        book=input("enter book name ")
                        author=input("enter author name ")
                        days=int(input("enter for how many days you want to issue it "))
                        finalday=days
                        issue=True
                        print("Book issue succesfully ")
                    case _:
                        print("invalid choice pelase enter valid choice ")
        case 3:

            if login==False:
                print("please rigister yourself first ")
            elif issue==False:
                print("plese issue your booke first ")
            else:
                print("WELCOME TO RETURN COUNTER ")
                if finalday>15:
                    rate=finalday*20
                    print("your Total Rante is ",rate)
                elif finalday>5 and finalday<=15:
                    rate=finalday*5
                    print("your total Rante is ",rate)
                elif finalday>=2 and finalday<=5:
                    rate=finalday*2
                    print("your Total rante is ",rate)
                else:
                    print("FREE FOR READING ")
        case 4:
            print("THANKYOU FOR YOUR TIME ")
            break
        
        case _:
            print("invalid choice please enter valid choice ")