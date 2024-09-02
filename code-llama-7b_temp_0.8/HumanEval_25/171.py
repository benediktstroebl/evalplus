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
    factor = 2
    result = []
    while factor * factor <= n:
        count = 0
        while n % factor == 0:
            count += 1
            n //= factor
        if count:
            result.append(factor)
        factor += 1
    if n > 1:
        result.append(n)
    return result

