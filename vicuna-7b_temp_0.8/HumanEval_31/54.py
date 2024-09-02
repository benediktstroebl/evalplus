

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
    # Prime numbers are those that are not divisible by any integer except 1 and itself.
    # 6 is prime because it can only be divided by 1 and itself.
    # 101 is prime because it can only be divided by 1 and itself.
    # 11 is prime because it can only be divided by 1 and itself.
    # 13441 is prime because it can only be divided by 1 and itself.
    # 61 is prime because it can only be divided by 1 and itself.
    # 4 is not prime because it can be divided by 1, 2, and itself.
    # 1 is not prime because it can be divided by 1, -1, and itself.
    return True
