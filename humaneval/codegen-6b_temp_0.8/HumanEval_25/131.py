from typing import List


def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appeares in factorization.
    Input number should be equal to the product of all factors
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    """
    assert isinstance(n, int) and n >= 0
    prime_factors = []
    while n > 1:
        max_factor = n - 1
        while max_factor > 1 and n % max_factor == 0:
            prime_factor = max_factor
            max_factor = max_factor - 1
            prime_factors += [prime_factor] * (n // prime_factor)
            n = n // prime_factor
    if n > 1:
        prime_factors += [n]
    return prime_factors

