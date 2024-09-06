

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # Check if n is prime
    if not n % 2:
        return n
    if n <= 3:
        return n
    # Check if n is divisible by 3
    if n % 3 == 0:
        return 3 * largest_prime_factor(n // 3)
    # Check if n is divisible by 4
    if n % 4 == 0:
        return 2 * largest_prime_factor(n // 4)
    # Continue the process until n is reduced to a prime
    r = 5
    while r % 2 == 0:
        r = r + 1
    while r < n:
        d = n // r
        if d % r == 0:
            n = d
            r = r + 1
        else:
            r = r + 6
    return r
