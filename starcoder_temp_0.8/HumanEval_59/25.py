

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    assert n > 1 and not is_prime(n)

    result = 1
    divisor = 2
    while divisor * divisor <= n:
        if n % divisor == 0:
            n //= divisor
            result = divisor
        else:
            divisor += 1
    if n > 1:
        result = n
    return result
