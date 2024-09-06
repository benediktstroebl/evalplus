

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

    # Only the first number is prime
    if n == 2:
        return True

    # All even numbers are composite
    if n % 2 == 0:
        return False

    # Find the square root of n and add 1
    sqrt_n = int(n ** 0.5) + 1

    # Start from 3 and check divisibility of n
    for i in range(3, sqrt_n, 2):
        if n % i == 0:
            return False

    return True
