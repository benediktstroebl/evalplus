

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # set up a list of primes less than or equal to the square root of n
    primes = [2, 3]
    i = 4
    while i*i <= n:
        if n % i == 0:
            primes.append(i)
        i += 1
    # loop over the primes
    for p in primes:
        # loop over the factors of n
        while n % p == 0:
            n //= p
        # if the factor is not 1, we've found the largest prime factor
        if n != 1:
            return p
    return 1

