

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    factors = []
    count = 1
    while count * count < n:
        if n % count == 0:
            factors.append(count)
        count += 1
    factors.append(n)
    for factor in reversed(factors):
        for other in factors:
            if other > factor and other % factor == 0:
                break
        else:
            return factor

    raise ValueError(f'largest_prime_factor({n}) does not terminate.')
