

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    if n < 1 or n % 2 == 0:
        return 1
    d = n - 1
    while d % 2 == 0:
        d = d / 2
    d = 3
    while True:
        if d > n:
            break
        for i in range(10, int(n**0.5) + 1, 2):
            if d % i == 0:
                break
        if d % i != 0:
            return i
        d = i + 2
    return d