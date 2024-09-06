

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    prime_factors = []
    divider = 2
    while n > 1:
        if n % divider == 0:
            prime_factors.append(divider)
            n //= divider
            divider = 2
        else:
            divider += 1
    return max(prime_factors)
