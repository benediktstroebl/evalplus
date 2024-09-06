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
    if n <= 0:
        raise ValueError("Input should be a positive integer")
    result = []
    while n % 2 == 0:
        n //= 2
        result.append(2)
    d = 3
    while d ** 2 <= n:
        if n % d == 0:
            n //= d
            result.append(d)
        else:
            d += 2
    if n != 1:
        result.append(n)
    return result

