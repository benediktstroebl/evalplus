

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
    # base cases
    if n < 2:
        return False
    if n == 2:
        return True
    if n == 3:
        return True
    
    # check if n is prime by testing divisibility by 2, 3, 4, and 5
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return False
    if n % 4 == 0:
        return False
    if n % 5 == 0:
        return False
    
    # if n is not divisible by 2, 3, 4, or 5, it is prime
    return True
