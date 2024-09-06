

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
    # take off the even numbers so that we don't need to check them
    if n % 2 == 0:
        return False
    # now check all odd numbers up to sqrt(n)
    m = 3
    while m * m <= n:
        if n % m == 0:
            return False
        m += 2
    return True
