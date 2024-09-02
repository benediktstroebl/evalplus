

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    "*** YOUR CODE HERE ***"
    assert n > 1, 'n must be greater than 1'
    i = n - 1
    while i > 1:
        if n % i == 0:
            n = n / i
        else:
            i = i - 1
    return n
