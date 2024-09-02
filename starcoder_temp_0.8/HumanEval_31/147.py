

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
    if n <= 3:
        return n > 1
    if not n % 2 or not n % 3:
        return False
    i = 5
    w = 2
    while i * i <= n:
        if not n % i:
            return False
        i += w
        w = 6 - w
    return True
