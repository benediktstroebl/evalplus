

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
    # special case of 2, which is always prime
    if n == 2:
        return True

    # loop through and check the divisors of all numbers less than sqrt(n)
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            return False

    # if we get here, n must be prime
    return True
