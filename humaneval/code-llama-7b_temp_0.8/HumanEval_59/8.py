

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    while n % 2 == 0:
        n //= 2
    if n % 4 == 3:
        n -= 1
    while n % 3 == 0:
        n //= 3
    while n > 1:
        div = 5
        while div ** 2 <= n:
            if n % div == 0:
                n //= div
            else:
                div += 6
        if n > 1:
            return n

