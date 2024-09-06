

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
    d, s = n - 1, 0
    while d % 2 == 0:
        d //= 2
        s += 1
    for a in range(5, int(math.sqrt(n)) + 1, 2):
        if n % a == 0:
            return False
    return True

