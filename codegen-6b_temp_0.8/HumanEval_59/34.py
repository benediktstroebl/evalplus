

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    trial_factor = 2
    factor = 1
    while trial_factor < n / trial_factor:
        if n % trial_factor == 0:
            factor = trial_factor
        trial_factor += 1
    return factor

