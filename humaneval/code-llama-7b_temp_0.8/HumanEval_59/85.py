

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # Let's get rid of all even factors
    # since they can't be prime
    while n % 2 == 0:
        n //= 2
    # Now n is odd, so it is good to test
    # only for odd numbers
    i = 3
    while i * i <= n:
        while n % i == 0:
            n //= i
        i += 2
    return n
