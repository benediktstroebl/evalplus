

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    factors = []
    for i in range(2, n + 1):
        if n % i == 0:
            break
    else:
        return n
    while n >= 2:
        if n % i == 0:
            break
        factors.append(i)
        n //= i
    return max(factors)
