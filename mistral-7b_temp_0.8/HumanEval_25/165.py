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
    while n != 1:
        result.append(2)
        while n % 2 == 0:
            n //= 2
        result.append(n)
        while n % 3 == 0:
            n //= 3
        result.append(n)
        while n % 5 == 0:
            n //= 5
        result.append(n)
        while n % 7 == 0:
            n //= 7
        result.append(n)
    return result
