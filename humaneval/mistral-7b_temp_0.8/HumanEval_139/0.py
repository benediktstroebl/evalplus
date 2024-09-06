
def special_factorial(n):
    """The Brazilian factorial is defined as:
    brazilian_factorial(n) = n! * (n-1)! * (n-2)! * ... * 1!
    where n > 0

    For example:
    >>> special_factorial(4)
    288

    The function will receive an integer as input and should return the special
    factorial of this integer.
    """
    # Your code here
    n=int(input("Enter a number: "))
    s=n
    count=1
    while count<=n:
        fact=n
        for i in range(1,count+1):
            fact=fact*(count-i+1)
            count=count+1
        s=s*fact
        print(s)
    print(s)
