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
    if len(factorize(n)) != 1:
        return []
    if (n & (n - 1)) == 0:
        return [n]
    m = n
    c = 1
    while n > 1:
        p = 1
        while n % 2 == 0:
            p = p * 2
            n = n // 2
        if p > m:
            break
        m = p
        c = c * p
    return [c, m]

