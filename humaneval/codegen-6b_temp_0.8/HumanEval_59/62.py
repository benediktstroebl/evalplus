

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    low = 2
    high = n
    while low < high:
        mid = (low + high) // 2
        if is_prime(mid):
            high = mid
        else:
            low = mid + 1
    return high
