

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    prime_factors = []
    count = 2
    while n > 1:
        if n % count == 0:
            prime_factors.append(count)
            n /= count
        else:
            count += 1
    return max(prime_factors)

