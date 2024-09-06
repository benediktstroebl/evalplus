

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    if n < 3 or not n % 2:
        return 2
    if n % 3 == 0:
        return 3
    if n > 3 and n % 2 == 0:
        return 4
    max_i = 5
    max_j = 6
    while True:
        while max_i <= n / max_i:
            if max_i > 2:
                max_i -= 2
            else:
                break
        while max_j <= n / max_j:
            if max_j > 3:
                max_j -= 2
            else:
                break
        if max_i > max_j:
            max_j = max_i + 2
        else:
            max_i = max_j + 2
    return max_i - 1
