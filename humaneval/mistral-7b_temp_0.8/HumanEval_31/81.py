

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
    # Is the number 2 or smaller?
    if n <= 1:
        return False

    # Start with 2 and iterate until we hit the square root of n
    for i in range(2, int(n ** 0.5) + 1):
        # If we can evenly divide n with i, then n is not prime
        if n % i == 0:
            return False

    # We have not found any integer that divides n with no remainder
    # So n must be prime
    return True

