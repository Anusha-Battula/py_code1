a=int(input("Enter 1st value: "))
b=int(input("Enter 2nd value: "))
print("Enter the operation you want to perform:\n 1.Add() \n 2.Sub() \n 3.Mul() \n 4.Div()\n")
c=input()
if(c=='1'):
    print(a+b)
elif(c=='2'):
    print(a-b)
elif(c=='3'):
    print(a*b)
elif(c=='4'):
    print(a//b)
else:
    print("Invalid Operater")
