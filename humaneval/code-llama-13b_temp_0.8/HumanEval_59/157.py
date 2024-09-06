

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # Inefficient way:
    # largest_prime = 2
    # while n % 2 == 0:
    #     n //= 2
    # i = 3
    # while n > 1:
    #     while n % i == 0:
    #         largest_prime = i
    #         n //= i
    #     i += 2
    # return largest_prime

    # Faster way:
    largest_prime = 1
    factor = 2
    while n > 1:
        while n % factor == 0:
            largest_prime = factor
            n //= factor
        factor += 1
    return largest_prime

