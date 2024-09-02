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
    ret = []

    while n % 2 == 0:
        ret.append(2)
        n //= 2

    c = 3
    while c <= n ** (1 / 2):
        if n % c == 0:
            while n % c == 0:
                ret.append(c)
                n //= c
        c += 2

    if n > 2:
        ret.append(n)

    return ret

