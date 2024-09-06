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
    """ Returns a list of prime factors of the input number.
    output: [(p1, exp1), (p2, exp2), ...]
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    """
    result = []
    div = 2
    while n >= div * div:
        exp = 0
        while n % div == 0:
            exp += 1
            n //= div
        if exp > 0:
            result.append((div, exp))
        div += 1

    if n > 1:
        result.append((n, 1))
    return result

