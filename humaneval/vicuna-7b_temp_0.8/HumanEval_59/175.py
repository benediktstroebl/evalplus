

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # Check for small cases
    if n <= 3:
        return 2
    
    # Check for prime numbers less than sqrt(n)
    for i in range(11, int(n ** 0.5) + 1):
        if n % i == 0:
            return 2
    
    # Try to find the largest prime factor
    for i in range(10, int(n ** 0.5) + 1):
        if n % i == 1:
            return i
    
    # Check for composite numbers
    if n != n % 2:
        return 2
    
    # Try to find the largest prime factor
    for i in range(int(n ** 0.5) + 1, n + 1):
        if n % i == 1:
            return i
    
    # Return 2 if no prime factor can be found
    return 2
