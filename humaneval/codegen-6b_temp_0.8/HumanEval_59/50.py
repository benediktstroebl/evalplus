

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    "*** YOUR CODE HERE ***"
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    i = 3
    while i <= n:
        while n % i == 0:
            factors.append(i)
            n //= i
        i += 2
    if len(factors) == 0:
        return n
    else:
        return max(factors)
