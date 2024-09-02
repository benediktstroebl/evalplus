

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    "*** YOUR CODE HERE ***"
    from math import sqrt
    i = 2
    while i <= sqrt(n):
        if n % i == 0:
            n = int(n / i)
            if n == 1:
                break
        else:
            i += 1
    return n
