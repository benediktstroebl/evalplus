

def is_prime(n):
    """Return true if a given number is prime, and false otherwise.
    >>> is_prime(6)
    False
    >>> is_prime(101)
    True
    >>> is_prime(11)
    True
    >>> is_prime(13441)
    True
    >>> is_prime(61)
    True
    >>> is_prime(4)
    False
    >>> is_prime(1)
    False
    """
    #remove the divisor 2, and we are left with only 1,3,5, and 7
    if n == 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    #we want to use the sieve method i.e. the range of numbers
    #we want all the numbers till n/2, so we use n/2
    #we skip even numbers
    for x in range(3, int(n/2), 2):
        if n % x == 0:
            return False
    return True
