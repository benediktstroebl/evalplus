

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    trial_div = 2
    while trial_div < n:
        if n % trial_div == 0:
            n = n // trial_div
        else:
            trial_div += 1
    return n

