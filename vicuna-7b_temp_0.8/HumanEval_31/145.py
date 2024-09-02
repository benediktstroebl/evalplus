

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
    # Avoid division by checking for n <= 2, which is a simple and fast test
    if n <= 2:
        return False
    # For larger values, check whether n is divisible by any of the prime numbers up to its square root
    # (we need not check 1, as 1 is always a prime)
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
