

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    from collections import defaultdict
    factors = defaultdict(int)

    def factorize(n: int) -> None:
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                factors[i] += 1
                n //= i
                factorize(n)
                return
        factors[n] += 1

    factorize(n)
    return max(factors.keys())

