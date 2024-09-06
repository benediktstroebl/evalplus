def largest_prime_factor(n):
    """Return the largest prime factor of n."""
    # Check for valid input
    if n < 2:
        raise ValueError("Input n must be greater than or equal to 2.")
    
    # Check if n is 1, returning 1 if it is
    if n == 1:
        return 1
    
    # Check if n is even, returning n if it is
    if n % 2 == 0:
        return n
    
    max_factor = n - 1
    while max_factor % 2 == 0:
        max_factor //= 2
    for factor in range(3, int(n ** 0.5) + 1, 2):
        while n % factor == 0:
            n //= factor
            if n == 1:
                return factor
    return n