
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    a = abs(a)
    if a < 100:
        for i in range(2,a):
            if a % i == 0:
                print(a,"is not a multiply prime number because ",a,"/",i,"=",a//i)
                return False
        print(a,"is a multiply prime number")
        return True
