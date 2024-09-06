

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # The largest prime factor of n is the largest prime p <= sqrt(n)
    # and where n % p == 0.
    # To determine if p is prime, it suffices to check that p is coprime with all integers <= sqrt(p).
    # This can be done in time O(sqrt(p)).

    # The following implementation uses "trial division" to test whether p is coprime with all integers
    # <= sqrt(p).

    # Implementation note:
    # It's easy to think of how to increment p.
    # But we can also increment exponentially:
    # if p is coprime with 31 integers <= sqrt(p),
    # then it is coprime with 2 * 31 = 62 integers <= sqrt(p),
    # etc.
    # The following procedure does this, and has running time O(sqrt(n)).
    p = 2
    while p ** 2 <= n:
        if n % p == 0:
            n //= p
        else:
            p += 1
    assert n == 1
    return p
