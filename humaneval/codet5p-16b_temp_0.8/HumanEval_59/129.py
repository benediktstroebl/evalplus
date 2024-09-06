

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """

    i = 2
    max_prime = 1
    while i * i <= n:
        if n % i == 0:
            max_prime = i
            n //= i
        else:
            i += 1
    if n > 1:
        max_prime = n
    return max_prime
