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
    # your task here

    # 素因数分解をする
    factor_list = []
    index = 2
    while n != 1:
        if n % index == 0:
            n /= index
            factor_list.append(index)
            index = 2
            continue
        index += 1

    return factor_list

