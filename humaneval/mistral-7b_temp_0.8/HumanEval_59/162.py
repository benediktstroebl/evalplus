

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    def gcd(m: int, n: int):
        """Compute the greatest common divisor of m and n. Assume m > n."""
        while n > 0:
            m, n = n, m % n
        return m

    while n % 2 == 0:
        n //= 2
    if n == 1:
        return 2
    for i in range(3, int(n ** 0.5) + 1, 2):
        while n % i == 0:
            n //= i
    return n

