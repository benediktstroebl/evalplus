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
    res = []

    while n % 2 == 0:
        n = n // 2
        res.append(2)

    factor = 3
    while n != 1 and factor * factor <= n:
        if n % factor == 0:
            n = n // factor
            res.append(factor)
        else:
            factor += 2 if factor > 2 else 1

    if n != 1:
        res.append(n)

    return res

