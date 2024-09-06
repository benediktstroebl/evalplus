

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    if n < 2:
        raise ValueError("n must be greater than 1")
    if n % 2 == 0:
        return 2
    x = 1000000
    y = 1
    while x < n:
        if x % 2 == 0:
            x *= 2
            continue
        for i in range(6, int(log(x, 2)) + 1, 2):
            if x % i == 0:
                x *= i
                continue
        if y * y > x:
            y *= x
        x = y
        y = 1
    return x
