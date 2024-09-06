

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
    # Only bother checking if n is positive
    if n <= 1:
        return False
    # Only bother checking if n is a prime if n is odd
    if n % 2 == 0:
        return False
    # Loop through the prime numbers less than or equal to n and check if n is divisible by any of them
    for p in range(1, int(n ** 0.5) + 1):
        if n % p == 0:
            return False
    return True
