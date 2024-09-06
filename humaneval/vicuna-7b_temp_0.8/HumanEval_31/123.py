

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
    # base case: if n is less than 2, it's clearly not prime
    if n < 2:
        return False

    # the number is prime if and only if it has no factors other than 1 and itself
    factors = [x for x in range(2, int(n**0.5) + 1) if n % x == 0]
    if not factors:
        return True

    # if the number has factors, it is not prime
    return False
