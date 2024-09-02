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
    if n < 1:
        raise ValueError(f"number should be a positive integer, not {n}")
    factors = [1]
    for factor in range(1, n+1):
        if factor <= n:
            factors.append(factor)
        while (n % factor == 0):
            factors[-1] *= factor
            n //= factor
    return factors

