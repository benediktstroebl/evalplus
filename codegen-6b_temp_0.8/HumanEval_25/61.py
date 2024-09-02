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
        raise ValueError("Factors can be found only for positive integers")
    if n == 1:
        return [1]
    if n == 2:
        return [2]
    # if n % 2 == 0:
    #     return [2] + factorize(n // 2)
    # get the smallest number that is higher than n / 2
    checknum = int(n / 2)
    # check whether checknum is a prime
    while checknum >= 3:
        if n % checknum == 0:
            return [checknum] + factorize(n // checknum)
        checknum -= 2
    return [checknum] + factorize(n // checknum)

