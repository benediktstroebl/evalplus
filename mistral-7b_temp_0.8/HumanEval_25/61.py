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
    if n < 0:
        n = abs(n)
    if n == 0:
        return [0]
    if n == 1:
        return [1]

    factors = []
    p = 2
    while p * p <= n:
        if n % p == 0:
            factors.append(p)
            n //= p
            while n % p == 0:
                n //= p
        else:
            p += 1

    if n > 1:
        factors.append(n)

    return factors

