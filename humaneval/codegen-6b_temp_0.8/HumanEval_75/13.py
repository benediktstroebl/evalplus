
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    a = abs(a)
    for i in range(2, a):
        if a % i == 0 and isPrime(i):
            b = a // i
            if isPrime(b) and b != 1:
                return True
    return False
