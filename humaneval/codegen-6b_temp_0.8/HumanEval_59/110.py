

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    assert n > 1
    largest = 1
    while n % 2 == 0:
        n //= 2
    for i in range(3, int(sqrt(n)), 2):
        while n % i == 0:
            n //= i
            largest = i
    if n > 1:
        largest = n
    return largest

