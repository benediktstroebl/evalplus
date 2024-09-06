

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
    # get an upper bound for n assuming n is a prime
    n_sqrt = n**0.5
    n_upper_bound = int(n_sqrt+1)
    # test candidate numbers
    for candidate in range(2, n_upper_bound):
        if n % candidate == 0:
            return False
    return True
