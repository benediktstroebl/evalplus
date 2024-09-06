

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    for k in range(2, n + 1):
        if n % k == 0:
            n /= k
            if is_prime(n):
                return int(n)
    raise ValueError("n must be greater than 1")
