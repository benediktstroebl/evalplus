

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    assert n >= 1 and not is_prime(n), 'n must be >= 1 and not a prime.'

    # 1.
    i = 2
    while n > 1:
        # 2.
        while n % i == 0:
            # 3.
            n /= i

        # 4.
        i += 1
        if i > n:
            # 5.
            i = 2
    # 6.
    return n

