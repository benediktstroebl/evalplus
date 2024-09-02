

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
    # n must be positive integer
    if n < 2:
        return False
    # n must not be prime if n <= 6, otherwise the number is not big enough
    if n <= 6:
        return not n%n
    # try divisibility by 2
    if n % 2 == 0:
        return False
    # try divisibility by 3
    if n % 3 == 0:
        return False
    # try divisibility by 4
    if n % 4 == 0:
        return False
    # try divisibility by 5
    if n % 5 == 0:
        return False
    # try divisibility by 6
    if n % 6 == 0:
        return False
    # try divisibility by 7
    if n % 7 == 0:
        return False
    # try divisibility by 8
    if n % 8 == 0:
        return False
    # try divisibility by 9
    if n % 9 == 0:
        return False
    # try divisibility by 10
    if n % 10 == 0:
        return False
    # if n is not divisible by any numbers from 2 to 9, then n is prime
    return True