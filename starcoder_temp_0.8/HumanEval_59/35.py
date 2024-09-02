

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    k = 2
    while True:
        if n % k == 0:
            n /= k
        else:
            k += 1
        if k * k > n:
            return n
