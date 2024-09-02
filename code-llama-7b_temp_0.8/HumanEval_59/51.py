

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # print("n", n)
    if is_prime(n):
        return n
    return largest_prime_factor(n // find_largest_divisor(n))

