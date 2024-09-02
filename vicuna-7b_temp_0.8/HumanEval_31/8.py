

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
    # Check if n is a prime number
    if not n % 2:
        return False
    if n % 3:
        return False
    for i in range(7, int(n ** 0.5) + 1, 2):
        if n % i:
            return False
    return True
