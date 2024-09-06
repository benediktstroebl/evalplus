

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    if n < 2:
        raise ValueError("n must be a positive integer")
    if n % 2 == 0:
        return 2
    max_val = 3
    max_index = 0
    for i in range(1, int(n**0.5) + 1, 2):
        if n % i == 0:
            break
        max_val = i
        max_index = int(n**0.5)
    return max_val