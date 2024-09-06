

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # Generates prime factors of n
    def factors(n):
        d = 2
        while d * d <= n:
            while (n % d) == 0:
                yield d
                n //= d
            d += 1
        if n > 1:
            yield n

    # Selects largest prime factor
    def largest_prime_factor(n):
        return max(factors(n))

    return largest_prime_factor(n)

