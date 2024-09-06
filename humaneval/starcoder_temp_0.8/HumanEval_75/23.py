
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    primes = [1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    for x in primes:
        if a % x == 0 and a / x in primes:
            return True
    return False
