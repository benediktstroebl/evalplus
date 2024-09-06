

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # first check if n is prime, if it is, return it
    if n > 1 and n % 2 == 0:
        return n
    # try to find the largest prime factor by factoring n
    # with the trial division method
    factors = []
    while True:
        for i in range(3, int(n**0.5) + 1, 2):
            for j in range(i + 1, int(n**0.5) + 1, 2):
                if n % (i * j) == 0:
                    break
        else:
            factors.append(i)
    if len(factors) == 1:
        return factors[0]
    else:
        # if there are multiple factors, take the largest one
        return max(factors)
