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
    if n < 2:
        return [n]
    while n % 2 == 0:
        n = n // 2
        result.append(2)
    i = 3
    while i ** 2 <= n:
        while n % i == 0:
            n = n // i
            result.append(i)
        i = i + 2
    if n > 1:
        result.append(n)
    return result

