

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    if n < 0:
        raise ValueError('n must be positive')

    # check if n is a prime number
    # if n > 1 and not any(n % i == 0 for i in range(2, n)):
    #     return n
    #
    # if n % 2 == 0:
    #     return largest_prime_factor(n // 2)
    #
    # for i in range(3, n, 2):
    #     if n % i == 0:
    #         return largest_prime_factor(i)
    #
    # return n

    # if n > 1:
    #     for i in range(2, n):
    #         if n % i == 0:
    #             n = n // i
    #     return n

    # return 1 if n <= 1 else n

    if n <= 1:
        return 1
    # for i in range(2, n):
    #     if n % i == 0:
    #         n = n // i
    
