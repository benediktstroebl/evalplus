

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    if n <= 1 or not n % 2:
        return 2
    max_prime = 3
    max_div = 5
    while True:
        if n % max_prime:
            break
        if n % (max_prime * max_div):
            max_prime = max_prime * max_div
        else:
            max_div = max_prime * 2
    return max_prime
