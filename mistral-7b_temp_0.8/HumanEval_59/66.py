

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    if n < 2:
        raise Exception("n must be greater than 1")
    if n % 2 == 0:
        return 2
    div = 3
    while div <= n:
        if n % div == 0:
            if is_prime(div):
                return div
            else:
                n /= div
        else:
            div += 2
    return n

