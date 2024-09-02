

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    if n > 1:
        n = int(n**0.5 + 1)
        while n > 2:
            if n % 2 == 0:
                break
            n = n - 1
        else:
            n = n + 1
        while n < n//2:
            n = next(prime for p in primes if n*p <= n)
        return n
    else:
        return 1
