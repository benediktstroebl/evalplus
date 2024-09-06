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
    "*** YOUR CODE HERE ***"
    factor_dict = {}

    while n % 2 == 0:
        factor_dict[2] = factor_dict.get(2, 0) + 1
        n /= 2
    if n == 1:
        return list(factor_dict.keys())
    while n % 3 == 0:
        factor_dict[3] = factor_dict.get(3, 0) + 1
        n /= 3
    if n == 1:
        return list(factor_dict.keys())
    while n % 5 == 0:
        factor_dict[5] = factor_dict.get(5, 0) + 1
        n /= 5
    if n == 1:
        return list(factor_dict.keys())
    while n % 7 == 0:
        factor_dict[7] = factor_dict.get(7, 0) + 1
        n /= 7
    if n == 1:
        return list(factor_dict.keys())
    if n != 1:
        factor_dict[n] = factor_dict.get(n, 0) + 1
        return list(factor_dict.keys())
