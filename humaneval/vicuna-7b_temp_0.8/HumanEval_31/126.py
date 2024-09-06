

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
    # Base case: if n is 2, it is prime
    if n == 2:
        return True

    # If n is not prime, it must be divisible by a number less than n
    for i in range(2, int(n ** 0.5) + 1):
        if not n % i:
            return False

    # If n is not divisible by any smaller number than itself, it is prime
    return True
