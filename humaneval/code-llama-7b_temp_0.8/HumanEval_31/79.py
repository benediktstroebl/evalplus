

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
    # Base cases
    if n < 2:
        return False
    if n < 4:
        return True

    # If n is divisible by 2 or 3, n is not prime
    if n % 2 == 0 or n % 3 == 0:
        return False

    # This is the definition of a prime number
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i = i + 6

    return True

