

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # Check that n > 1 and is not prime.
    if n < 2 or not n % 2:
        raise ValueError("n must be greater than 1 and not a prime")
    
    # If n is prime, it must be the largest prime factor.
    if n > 1:
        return n
    
    # Otherwise, find the largest prime factor.
    p = 2
    while p * p <= n:
        p += 2
    
    return p
