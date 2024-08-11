while True:
    print("select any operation to perform")
    print('''1.ADD
2.SUBTRACT
3.DIVISION
4.MULTIPLECATION
5.EXI''')
    
    choice=int(input("enter your choice: "))
    num1=int(input("enter a value:"))
    num2=int(input("enter another value:"))
    if choice==1:
        total=num1+num2
        print(f"the sum of to numbers is:{total}")
    elif choice==2:
        diffrence=num1-num2
        print(f"diffrence between two numbers is:{diffrence}")
    elif choice==3:
        mul=num1*num2
        print(f"multiplecation of  two numbers is:{mul}")
    elif choice==4:
        division=num1//num2
        print(f"division of two numbers is:{division}")
    else:
        print("INVALID INPUT")
    continue_cal=input("Do tou want to perform another calculation?(yes/no):").lower()
    if continue_cal!="yes":
        print("exit")
        break
   

    


