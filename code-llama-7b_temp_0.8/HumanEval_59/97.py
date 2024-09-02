

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    largest = 2
    while largest <= n // 2:
        if n % largest == 0:
            n //= largest
        else:
            largest += 1
    return int(n)
