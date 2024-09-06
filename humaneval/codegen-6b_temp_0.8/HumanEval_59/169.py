

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    max = n - 1
    while max % 2 == 0:
        max //= 2
    
    max = max // 2 + 1
    
    while max != 1:
        if n % max == 0:
            return max
        
        max -= 1
    
    return n
