

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
    # Primes can only be odd numbers, so start with an even number
    # and check if it is divisible by any number less than or equal to sqrt(n).
    # If not, it's prime.
    if n % 2 == 0:
        return False
    if n <= int(sqrt(n)) + 1:
        return False
    if n % n - n:
        return True
    for num in range(2, int(n**0.5) + 1):
        if n % num == 0:
            return False
    return True
