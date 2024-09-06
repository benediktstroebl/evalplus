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
    # factorize 70
    # 70 = 2 * 35 = 2 * 5 * 7
    # 2, 2, 5, 5, 7
    # put 2 and 5 to the list
    # 35 = 5 * 7
    # 5, 5, 7
    # 2, 2, 5, 5, 7
    # add 2
    # 7
    # 2, 2, 5, 5, 7
    # add 7
    # 2, 2, 5, 5, 7
    # 70

    # factorize 100
    # 100 = 2 * 50 = 2 * 2 * 25 = 2 * 2 * 5 * 5 = 2, 2, 2, 2, 5, 5
    # put 2, 2 to the list
    # 50 = 2 * 25 = 2 * 5 * 5 = 2
