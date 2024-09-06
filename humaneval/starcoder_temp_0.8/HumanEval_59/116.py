

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    result = 2

    while result * result <= n:
        if n % result == 0:
            n = n // result
        else:
            result += 1

    if n > 1:
        return n

    return result

