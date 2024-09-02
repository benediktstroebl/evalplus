

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

    
    import math
    if n <= 1:
        return False
    if n % 2 == 0 and n > 2:
        return False
    x = 3
    while x < math.sqrt(n) + 1:
        if n % x == 0:
            return False
        x += 2
    return True
    
    
