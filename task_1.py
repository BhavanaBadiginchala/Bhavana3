
def fact(n):
    if n<2:
        return 1
    else:
        return n * (fact(n-1))
    
num = int(input("Enter a number: "))
result = fact(num)
print("Factorial of %d is: %d "%(num,result))