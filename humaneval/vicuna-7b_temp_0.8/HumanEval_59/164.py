

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # Ensure n > 1 and not prime
    if n < 2 or not n % 2:
        return 2
    
    # Initialize variables
    p = 2
    while p < n:
        # Check for composite numbers
        if n % p:
            break
        
        # Increment p
        p = p + 2
    
    # If p is prime, return it
    return p
