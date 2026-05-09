print("WELCOME TO RASHAN DUKKAN")
finalname=""
finalFamilyId=""
addharId=0
flag=False
verify=False
sugar=False
while True:
    print()

    print("1 REgistration ")
    print(" 2 verification  ")
    print(" 3 fodd distribution  ")
    print(" ")
    choice=int(input("eneter your choice "))
    print()
    match choice:
        case 1:
            print("welcome to GOVT RASHAN DUKKAN ")
            name=input("enter your name ")
            lastName=input("enter your last name ")
            person=int(input("enter how many family memebr you have "))
            familyId=input("enter smagar id ")
            addhar=int(input("enter your addhar id"))
            finalname=name+lastName
            finalFamilyId=familyId
            addharId=addhar
            flag=True
            print("you register successfully on govt RAshan DUKAN")
            print()
        case 2:
            if flag==False:
                print("PLEASE REGISTER YOUR SELF FIRST ")
            else:
                print()
                print(f"welcome {finalname} you are verify now ")
                
                verify=True
        
        case 3:
            if flag==False:
                print("please register yourself first ")
            elif verify==False:
                print("you are not verifyied usser ")
            else:
                print()
                print("what you want ")
                print(" 1 pulses ")
                print(" 2 rice  ")
                print(' 3 wheat ')
                print(" 4 sugar  ")
                print(" 5 oil ")
                maxProduct=4
                choice1=int(input('enter your choice what you want '))
                match choice1:
                    case 1:
                        print("you can opt only 3 pulse at a time ")
                        count=3
                        print("1 for chana dal")
                        print("2 TOOR DAL ")
                        print(" 3 MOONG DALL ")
                        choice3=int(input('enter wich pulse you want '))
                        match choice3:
                            case 1:
                                if count>0:
                                    kg=int(input('enter your KG '))

                                    print("you have succesfully buy CHAANA DAL ")
                                    count-=1
                                else:
                                    print("you have reached your limit ")
                            case 2:
                                if count>0:
                                    kg=int(input('enter your KG '))

                                    print("you have succesfully buy TOOR  DAL ")
                                    count-=1
                                else:
                                    print("you have reached your limit ")
                            case 3:
                                if count>0:
                                    kg=int(input('enter your KG '))

                                    print("you have succesfully buy MOONG DAL ")
                                    count-=1
                                else:
                                    print("you have reached your limit ")
                            case _:
                                print("invalid choice please enter valid choice ")
                    case 2:
                        print('RICE IS VERY ESSENTIAL FOOD ')
                        maxRice=4
                        kg=int("enter kg for rice ")
                        if kg>maxRice:
                            print('you can only buy 4kg rice ')
                        else:
                            print("you have succefully bou rice ")
                    case 3:

                        print("wheat is very important food ")
                        maxwheat=10
                        kg=int(input('enter kg '))
                        if kg>maxwheat:
                            print("you can purchase only 10 kg ")
                        else:
                            print("you have succsfully bought wheat ")
                    case 4:
                        print("ADD SOME SWEET INTO YOUR LIFE ")
                        maxSugar=5
                        kg=int(input('enter sugar in kg '))
                        if kg>maxSugar:
                            print("you can only order 5 kg ")
                        else:
                            print("you have succesfully buy sugar ")
                            sugar=True
                    case 5:
                        if sugar==True:
                            print("you have bought sugar so you can not buy oil ")
                        else:
                            maxliter=15

                            liter=int(input("enter oil in liter "))
                            if liter>maxliter:
                                print(f"you can only buy{maxliter}")
                            else:
                                print("you have succefully but oil")
                    case _:
                        print("invalid choice please enter \n pleas eneter valid option")

                        


            

            
                


        


        
