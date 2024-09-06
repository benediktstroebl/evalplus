

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
    "*** YOUR CODE HERE ***"

    def is_prime_inner(n, x):
        if n == 1 or x == 1:
            return False
        if n % x == 0:
            return False
        return is_prime_inner(n, x - 1)

    return is_prime_inner(n, n - 1)

