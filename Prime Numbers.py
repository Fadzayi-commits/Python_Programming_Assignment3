num = int(input("Enter num: "))
if num > 1:
    for i in range(2, num//2):
        if(num % 1) == 0:
         print(num, "is not prime number")
         break
else:
    print("It's a prime number")