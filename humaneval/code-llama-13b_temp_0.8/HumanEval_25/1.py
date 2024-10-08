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

    factor = []
    while n % 2 == 0:
        n = n // 2
        factor.append(2)
    n3 = 3
    while n > 1:
        if n % n3 == 0:
            n = n // n3
            factor.append(n3)
        else:
            n3 += 2
    return factor

