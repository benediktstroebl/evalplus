
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    import math
    def isPrime(x):
        if x <= 1:
            return False
        elif x <= 3:
            return True
        elif x % 2 == 0 or x % 3 == 0:
            return False
        j = 5
        while j * j <= x:
            if x % j == 0 or x % (j + 2) == 0:
                return False
            j += 6
        return True
    # your code goes here
    for i in range(2, a):
        if isPrime(i) and isPrime(a // i) and isPrime(a // (i * (a // i))):
            return True
    return False
























