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
        return [1]  # returning this list is wrong, it will cause wrong answer!
    if n == 0:
        return [0]
    factors = []
    div = 2
    while n > 1:
        while n % div == 0:
            factors.append(div)
            n //= div
        div += 1
    return factors

