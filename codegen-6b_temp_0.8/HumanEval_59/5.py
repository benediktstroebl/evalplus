

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    p = 2
    i = 2
    while i <= n:
        if n % p == 0:
            n //= p
            break
        i = p
        p += 1
        print(p)
    return n

