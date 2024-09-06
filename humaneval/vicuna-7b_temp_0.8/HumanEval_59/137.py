

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # Ensure that n is not a prime by checking the first few prime factors.
    # This is a simple heuristic that should work well for large numbers.
    if n <= 1000000:
        return 1
    sqrt_n = int(np.sqrt(n))
    is_prime = n > 1
    for x in range(2, int(n**0.5) + 1):
        if n % x == 0:
            is_prime = False
            break
    if is_prime:
        return n
    for i in range(2, int(n**0.5) + 1, sqrt_n):
        if n % i == 0:
            is_prime = False
            break
        if n % i == 1:
            is_prime = False
            break
    return max(i, int(n**0.5) + 1)
