

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    "*** YOUR CODE HERE ***"
    if n < 2:
        return (None)
    elif n % 2 == 0:
        return (2)
    else:
        limit = n / 2
        while limit > 3:
            limit /= 2
            if n % limit == 0:
                return (limit)
        if n <= 3:
            return (3)
