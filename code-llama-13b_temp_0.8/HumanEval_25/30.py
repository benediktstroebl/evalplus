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
    num = n
    i = 2
    while i * i <= n:
        while num % i == 0:
            factor.append(i)
            num //= i
        i += 1
    if num > 1:
        factor.append(num)
    return factor

