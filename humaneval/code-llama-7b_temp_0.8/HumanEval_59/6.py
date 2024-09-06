

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    largest = 1
    d = n
    while (d % 2 == 0):
        largest = 2
        d = d // 2
    for i in range(3, int(n**0.5) + 1, 2):
        while (d % i == 0):
            largest = i
            d = d // i
    if (d > 1):
        largest = d
    return largest
