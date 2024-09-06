

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
    return n == 1 or n == 2 or n % 2 == 0
    # in this case, we can also add:
    # or n % 2 == 0
    # to exclude odd primes
    # or n == 0
    # to exclude even numbers greater than 2

