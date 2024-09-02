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
        return []
    elif n == 1:
        return [1]
    elif n == 2:
        return [2]
    elif n == 3:
        return [3]
    elif n % 2 == 0:
        return []
    factor = 5
    factors = []
    while factor * factor <= n:
        if n % factor == 0:
            while n % factor == 0:
                n = n // factor
                factors.append(factor)
        factor += 2
    if n > 1:
        factors.append(n)
    return factors

