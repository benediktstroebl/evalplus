

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    p = 2
    while p*p < n:
        if n % p!= 0:
            p += 1
        else:
            n /= p
    if n > 1:
        return n
    else:
        return
