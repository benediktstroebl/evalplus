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
    array = []
    if n % 2 == 0:
        array.append(2)
        n //= 2
    while n % 2 == 0:
        array.append(2)
        n //= 2
    for x in range(3, int(n ** (1 / 2)), 2):
        if n % x == 0:
            array.append(x)
            n //= x
    if n > 2:
        array.append(n)
    return array

