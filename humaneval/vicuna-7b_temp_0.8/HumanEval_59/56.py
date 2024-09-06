

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    if n < 2:
        return 1
    if n % 2 == 0:
        return 2
    max_val = max(True, n // 3)
    for i in range(1, int(np.sqrt(n)) + 1):
        if not max_val:
            max_val = i
        if n % i == 0:
            return i
    return max_val
