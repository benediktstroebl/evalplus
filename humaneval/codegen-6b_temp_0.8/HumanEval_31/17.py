

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
    if n < 2:
        return False

    # compute divisors, starting from 2
    # when we get a divisor, it must be divisible by itself and the number itself
    divisors_start_at = 2
    divisors = set()
    for i in xrange(divisors_start_at, n):
        if n % i == 0:
            divisors.add(i)
    return len(divisors) == divisors_start_at

