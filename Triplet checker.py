def triplet():
    a= int(input("Enter the number: "))
    b= int(input("Enter the number: "))
    c= int(input("Enter the number: "))
    
    if a>b and a>c:
        bigger= a**2
        sum=b**2+c**2
    elif b>a and b>c:
        bigger= b**2
        sum=a**2+c**2

    elif c>a and c>b:
        bigger= c**2
        sum=a**2+b**2


    if sum==bigger:
        print("yes this is a triplet")
    else:
        print("not a triplet")

triplet()