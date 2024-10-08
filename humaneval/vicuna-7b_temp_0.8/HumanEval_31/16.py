

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
    # Try the trivial case first (n=0 or 1)
    if n < 2:
        return False
    # Try the case where n is 2
    if n == 2:
        return True
    # Try the case where n is a prime
    if n > 2 and n % 2 == 0:
        return False
    # Try the case where n is composite (not prime)
    if n > 2 and n % 3 == 0:
        return False
    # Try the case where n is composite (not prime)
    for num in range(4, int(n**0.5) + 1, 2):
        if n % num == 0:
            return False
    return True
