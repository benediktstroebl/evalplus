

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # Divide by two to check even number because it is faster than modulo.
    x = n // 2
    while x * x <= n:
        if n % x == 0:
            n //= x
        else:
            x -= 1
    return n

