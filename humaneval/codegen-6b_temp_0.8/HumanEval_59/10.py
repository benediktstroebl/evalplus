

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    i = 2
    while i*i <= n:
        if n % i == 0:
            # n is divisible by i, try next
            n = n/i
        else:
            # n is NOT divisible by i, we have found the largest prime factor
            i += 1
    return n
