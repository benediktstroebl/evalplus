

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

    assert n > 1, "Input must be a positive integer."
    assert type(n) == int, "Input must be a positive integer."
    divisors = [i for i in range(n-1, 1, -1) if n % i == 0]
    if len(divisors) == 1:
        return True
    else:
        return False
