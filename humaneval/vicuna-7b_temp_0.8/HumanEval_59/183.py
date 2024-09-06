

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    factors = factorint(n)
    i = 0
    while i < len(factors) and isprime(factors[i]):
        i += 1
    if i == len(factors):
        return n
    while i < len(factors) and not isprime(factors[i]):
        if factors[i] > factors[i - 1]:
            i += 1
        else:
            break
    return factors[i]