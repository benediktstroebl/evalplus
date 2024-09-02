

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """

    if n == 1:
        return 1
    
    max_factor = n
    while n % 2 == 0:
        max_factor = 2
        n /= 2

    i = 3
    while i * i <= n:
        if n % i == 0:
            max_factor = i
            n /= i
        i += 2

    if n > 1:
        max_factor = n

    return max_factor
