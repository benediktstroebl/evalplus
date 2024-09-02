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
    if n == 1: return [1]
    if n == 2: return [2]
    if n <= 3: return [n]
    if n & 1 == 0:
        return factorize(n >> 1) + factorize(n >> 1)
    d = 3
    while d * d <= n:
        if n % d == 0:
            return factorize(n // d) + [d]
        d += 2
    return factorize(n - 1) + [n]

