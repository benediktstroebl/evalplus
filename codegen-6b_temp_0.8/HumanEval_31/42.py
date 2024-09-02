

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
    
    # If n is 0, or 1, it is not prime
    if n == 1 or n == 0:
        return False
    # If n is even, it is not prime
    elif n % 2 == 0:
        return False
    # else check for all odd factors
    else:
        for j in range(3, math.floor(math.sqrt(n)) + 1, 2):
            if n % j == 0:
                return False
        return True
    