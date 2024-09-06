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

    assert n > 0, "Only positive numbers will be handled."
    result = []
    p = 2
    while p * p <= n:
        if n % p!= 0:
            p += 1
        else:
            n //= p
            result.append(p)
    if n > 1:
        result.append(n)
    return result

