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
    factor_list = []
    while n > 0 and n % 2 == 0:
        factor_list.append(2)
        n = n // 2
    while n > 0 and n % 5 == 0:
        factor_list.append(5)
        n = n // 5
    factor = 7
    while n > 1:
        if n % factor == 0:
            factor_list.append(factor)
            n = n // factor
        else:
            factor = factor + 2
    return factor_list

