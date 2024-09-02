

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # max_prime = 2
    # while max_prime * max_prime < n:
    #     max_prime += 2
    # i = max_prime - 2
    # while i > 1:
    #     if n % i == 0:
    #         n = n // i
    #     else:
    #         i -= 2
    # return n
    max_prime = 1
    while n % 2 == 0:
        n = n // 2
        max_prime = 2
    i = 3
    while i * i <= n:
        if n % i == 0:
            n = n // i
            max_prime = i
        else:
            i += 2
    return max_prime

