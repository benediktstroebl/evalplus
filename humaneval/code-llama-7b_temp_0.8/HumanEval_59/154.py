

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    primes = []
    for i in range(2, n + 1):
        if n % i == 0:
            primes.append(i)
        else:
            continue
    for prime in primes:
        if is_prime(prime):
            return prime

