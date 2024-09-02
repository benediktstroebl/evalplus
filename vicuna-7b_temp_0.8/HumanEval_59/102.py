

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    if n < 3:
        return 2
    
    # find factors
    factors = [n]
    while n > 1:
        for i in range(1, int(n**0.5) + 1):
            for j in range(i**2, n+1, i):
                factors.append(j)
        n = factors[0]
    
    # find largest prime factor
    largest_prime = None
    largest_val = 0
    for i in factors:
        if i > 1 and i % 2 == 0:
            continue
        if i > largest_prime:
            largest_prime = i
            largest_val = max(largest_val, i)
    
    return largest_val
