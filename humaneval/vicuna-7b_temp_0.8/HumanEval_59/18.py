

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    if n < 1 or not n % 2 or n % 3:
        return 2
    p = 5
    max_val = 3
    while True:
        if p * p > n:
            break
        if n % p == 0:
            break
        p += 1
    if n % p == 0:
        p = max_val
    while n % p == 0:
        p += 1
        if p > max_val:
            max_val = p
    return max_val
