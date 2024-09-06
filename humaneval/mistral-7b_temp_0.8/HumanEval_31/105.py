

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
    # An even number is not prime
    if not n % 2:
        return False
    # If n has more than 2 factors it is not prime
    for i in range(3, int(n**0.5)+1, 2):
        if not n % i:
            return False
    return True
