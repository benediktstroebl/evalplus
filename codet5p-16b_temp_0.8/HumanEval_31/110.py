

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
    if n < 2:
        return False
    else:
        for i in range(2, math.floor(math.sqrt(n))+1):
            if n%i == 0:
                return False
        return True
    
