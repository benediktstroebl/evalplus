

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # copy n, since we will be dividing n by 2,
    # and we don't want to modify the original n
    n_copy = n

    while n_copy % 2 == 0:
        # keep dividing n by 2 until it is no longer even
        n_copy //= 2

    # keep dividing n by the number of the prime factors
    # until it is no longer divisible by those prime factors
    i = 3
    while i*i <= n_copy:
        while n_copy % i == 0:
            n_copy //= i
        i += 2

    # if n is still divisible by 1, it is prime (since the only prime factors left are 1 and itself)
    return n if n_copy % 1 == 0 else n_copy

