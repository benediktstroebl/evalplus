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
    if (n < 2):
        return []
    if (n == 2):
        return [2]
    if (n == 1):
        return [1]
    if (n % 2 == 0):
        return [2] + factorize(n // 2)
    if (n % 3 == 0):
        return [3] + factorize(n // 3)
    if (n % 5 == 0):
        return [5] + factorize(n // 5)
    l = []
    while n % 2 == 0:
        l.append(2)
        n //= 2
    if (n != 1):
        l.append(n)
    return l

