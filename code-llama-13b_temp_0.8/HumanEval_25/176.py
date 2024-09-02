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
    if n <= 0:
        raise ValueError("Input number should be greater than zero")
    elif n == 1:
        return []

    factor_list: List[int] = []

    i = 2

    while i ** 2 <= n:
        if n % i == 0:
            n = n // i
            factor_list.append(i)
        else:
            i += 1

    if n > 1:
        factor_list.append(n)

    return factor_list

