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

    if n == 1:
        return [1]

    factors = []
    div = 2
    while div * div <= n:
        if n % div == 0:
            factors.append(div)
            n //= div
        else:
            div += 1
    factors.append(n)
    return factors

