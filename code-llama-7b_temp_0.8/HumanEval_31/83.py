

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
    if n == 2:
        return True
    elif n < 2 or not n & 1:
        return False

    sqrt_n = int(n ** 0.5) + 1
    for m in range(3, sqrt_n, 2):
        if n % m == 0:
            return False

    return True

