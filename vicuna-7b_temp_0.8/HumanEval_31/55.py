

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
    # Check if n is prime
    if n > 2:
        # Check if n has any factors other than 1 and n
        if n % 1 == 0 or n % 2 == 0:
            return False
        for x in range(3, int(n**0.5) + 1, 2):
            if n % x == 0:
                return False
        return True
    else:
        return False
