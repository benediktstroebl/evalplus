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
        return []
    if n == 1:
        return [n]
    for i in range(2, int(n**0.5) + 1):
        for j in range(i**2, n+1, i):
            if n % j == 0:
                return [int(j), ] + factorize(n//j)[1:]
    return []
