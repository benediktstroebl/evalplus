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
    if n <= 1:
        return []

    factors = [n]
    while n % 2 == 0:
        factors.append(2)
        n = n // 2

    for factor in range(3, int(math.sqrt(n)) + 1, 2):
        while n % factor == 0:
            factors.append(factor)
            n = n // factor

    if n > 1:
        factors.append(n)

    return
