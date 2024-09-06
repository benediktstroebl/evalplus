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
        return []
    if n < 0:
        return []

    s = 1
    while s < n:
        s *= 2

    factors = [2]
    s = 3
    while s < s/2 + 1:
        if n % s == 0:
            factors.append(s)
            n //= s
            s = 3
        else:
            s += 2

    if n > 2:
        factors.append(n)

    return factors

