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
    d = 2
    while n != 1:
        if d > n:
            if n % d == 0:
                n //= d
                result.append(d)
            else:
                break
        if n % d == 0:
            n //= d
            result.append(d)
        d += 1
    return result

