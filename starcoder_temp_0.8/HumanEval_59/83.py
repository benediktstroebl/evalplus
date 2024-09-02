

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    
    max_factor = n // 2
    
    for factor in range(2, max_factor + 1):
        if n % factor == 0:
            n = n // factor
            max_factor = n
            break
    
    return factor
