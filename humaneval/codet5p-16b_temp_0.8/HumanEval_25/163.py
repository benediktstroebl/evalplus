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
    if n == 1:
        return [1]
    while n % 2 == 0:
        factor.append(2)
        n = n / 2
    while n % 3 == 0:
        factor.append(3)
        n = n / 3
    i = 5
    while i * i <= n:
        if n % i == 0:
            factor.append(i)
            n = n / i
        else:
            i += 2
    if n > 2:
        factor.append(int(n))
    return factor

