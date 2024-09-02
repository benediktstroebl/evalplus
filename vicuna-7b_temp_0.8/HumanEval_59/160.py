

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # try to find a prime factor by dividing n-1 by known primes
    for i in range(10, 10001):
        if n - 1 % i == 0:
            # if n-1 has a factor smaller than i, n must also have that factor
            # and it is the largest prime factor
            return i
        if i > n // i:
            # if we're trying to find the largest prime factor of n,
            # we don't care about i itself being prime
            break
    # if n does not have a prime factor smaller than 10,
    # the largest prime factor must be 10 or greater
    return 10
