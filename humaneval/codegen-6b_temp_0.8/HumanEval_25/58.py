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
    if n == 0 or n == 1:
        return [0]

    factor_list = []
    factor = 2
    while factor * factor < n:
        if n % factor:
            factor += 1
        else:
            n //= factor
            factor_list.append(factor)

    if n > 1:
        factor_list.append(n)

    return factor_list

