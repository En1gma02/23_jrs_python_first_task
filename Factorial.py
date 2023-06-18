print("Akshansh Dwivedi")

num= input("Enter a number: ")
factorial= int(1)
if num.isdigit():
    num= int(num)
    if num==0:
        print("Factorial = 1")
    else:
        while num>1:
            factorial= factorial*(num)
            num= (num-1)
        print("Factorial = ", factorial)
else:
    print("Not a valid input")
