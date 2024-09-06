

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
    # Large prime number for test
    p = 100000000

    # Small number for test
    q = 2

    # Smallest number that can be divided by p (we use this to check if p is prime)
    d = 2

    while d * d <= p:
        if p % d == 0:
            return False
        d += 1

    return True
