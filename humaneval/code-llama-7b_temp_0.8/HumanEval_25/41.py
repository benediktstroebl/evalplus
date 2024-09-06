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
    result = []
    if n < 2:
        return [n]
    while n % 2 == 0:
        n = n / 2
        result.append(2)
    if n == 1:
        return result
    p = 3
    while n > p:
        while n % p == 0:
            n = n / p
            result.append(int(p))
        p = p + 2
    result.append(int(n))
    return result

